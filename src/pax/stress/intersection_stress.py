"""Intersection-owned stress model and diagnostics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from shapely.geometry import Point

from pax.scripts.voronoi_stress_scoring import calculate_weighted_stress


@dataclass(frozen=True)
class IntersectionStressDiagnostics:
    node_id: int
    coord: tuple[float, float]
    base_source: str
    base_stress: float
    neighbor_stress: float
    second_order_stress: float
    total_stress: float
    fallback_used: bool
    stress_source_key: str
    stress_path_id: str
    neighbor_summary: dict[str, Any]
    second_order_summary: dict[str, Any]
    zone_index: int | None = None
    camera_id: str | None = None


@dataclass
class IntersectionStressModel:
    intersection_stress: dict[int, float]
    diagnostics: dict[int, IntersectionStressDiagnostics]
    stress_source_key: str
    stress_path_id: str

    def get_scalar(self, node_id: int) -> float:
        return self.intersection_stress.get(node_id, 0.0)

    def build_route_diagnostics(
        self,
        route_nodes: list[int],
        graph: Any,
        stress_weight: float,
    ) -> dict[str, Any]:
        intersections = [
            self.diagnostics[node_id].__dict__
            for node_id in route_nodes
            if node_id in self.diagnostics
        ]
        edges = []
        for i in range(len(route_nodes) - 1):
            u = route_nodes[i]
            v = route_nodes[i + 1]
            edge_length = graph.get_edge_weight(u, v)
            edge_stress = 0.5 * (self.get_scalar(u) + self.get_scalar(v))
            edges.append(
                {
                    "edge_u": u,
                    "edge_v": v,
                    "edge_length": edge_length,
                    "edge_stress": edge_stress,
                    "stress_penalty": edge_stress * stress_weight,
                }
            )
        return {
            "stress_path_id": self.stress_path_id,
            "stress_source_key": self.stress_source_key,
            "intersections": intersections,
            "edges": edges,
        }

    @classmethod
    def from_precomputed(
        cls,
        intersection_stress: dict[int, float],
        graph: Any,
        stress_source_key: str,
        stress_path_id: str,
        base_source: str,
    ) -> "IntersectionStressModel":
        diagnostics: dict[int, IntersectionStressDiagnostics] = {}
        for node_id, value in intersection_stress.items():
            coord = graph.intersections.get(node_id, {}).get("original_coord", (0.0, 0.0))
            diagnostics[node_id] = IntersectionStressDiagnostics(
                node_id=node_id,
                coord=tuple(coord),
                base_source=base_source,
                base_stress=float(value),
                neighbor_stress=0.0,
                second_order_stress=0.0,
                total_stress=float(value),
                fallback_used=False,
                stress_source_key=stress_source_key,
                stress_path_id=stress_path_id,
                neighbor_summary={"count": 0, "total": 0.0},
                second_order_summary={"count": 0, "total": 0.0},
            )
        return cls(
            intersection_stress=intersection_stress,
            diagnostics=diagnostics,
            stress_source_key=stress_source_key,
            stress_path_id=stress_path_id,
        )

    @classmethod
    def from_voronoi_zones(
        cls,
        graph: Any,
        zones_gdf: Any,
        neighbors: dict[int, list[int]],
        camera_stress: dict[str, float],
        neighbor_weight: float,
        second_order_weight: float,
        transformer: Any,
        stress_source_key: str,
    ) -> "IntersectionStressModel":
        diagnostics: dict[int, IntersectionStressDiagnostics] = {}
        stress_map: dict[int, float] = {}
        for node_id, inter_data in graph.intersections.items():
            coord = inter_data.get("original_coord", [])
            if not coord or len(coord) < 2:
                continue
            point = Point(coord[0], coord[1])
            weighted = calculate_weighted_stress(
                point=point,
                zones_gdf=zones_gdf,
                neighbors=neighbors,
                camera_stress=camera_stress,
                neighbor_weight=neighbor_weight,
                second_order_weight=second_order_weight,
                transformer=transformer,
            )
            neighbor_contribs = weighted["contributions"]["neighbors"]
            second_contribs = weighted["contributions"]["second_order"]
            neighbor_summary = {
                "count": len(neighbor_contribs),
                "total": sum(item["weighted_stress"] for item in neighbor_contribs),
            }
            second_summary = {
                "count": len(second_contribs),
                "total": sum(item["weighted_stress"] for item in second_contribs),
            }
            total = float(weighted["total_weighted_stress"])
            stress_map[node_id] = total
            diagnostics[node_id] = IntersectionStressDiagnostics(
                node_id=node_id,
                coord=(coord[0], coord[1]),
                base_source="voronoi_zone",
                base_stress=float(weighted["base_stress"]),
                neighbor_stress=float(weighted["neighbor_stress"]),
                second_order_stress=float(weighted["second_order_stress"]),
                total_stress=total,
                fallback_used=weighted.get("fallback_used", False),
                stress_source_key=stress_source_key,
                stress_path_id="intersection_stress:voronoi_neighbor_weighted",
                neighbor_summary=neighbor_summary,
                second_order_summary=second_summary,
                zone_index=weighted["zone_index"],
                camera_id=weighted["camera_id"],
            )
        return cls(
            intersection_stress=stress_map,
            diagnostics=diagnostics,
            stress_source_key=stress_source_key,
            stress_path_id="intersection_stress:voronoi_neighbor_weighted",
        )
