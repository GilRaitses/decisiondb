#!/usr/bin/env python3
"""Parity test for intersection stress refactor (OD 85 -> 50)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import geopandas as gpd

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from pax.pathfinding.learned_heuristic import LearnedHeuristicPathfinder
from pax.scripts.voronoi_stress_scoring import find_neighbors, project_zones_for_distance
from pax.stress.intersection_stress import IntersectionStressModel
from pax.stress.stress_reader import resolve_camera_stress_map


def load_trace(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def main() -> int:
    trace_path = PROJECT_ROOT / "scripts" / "2026-01-16" / "artifacts" / "traces" / "pearson_stress_activation_trace.json"
    trace = load_trace(trace_path)

    stress_scores_path = PROJECT_ROOT / "data" / "stress_scores_updated.json"
    zones_path = PROJECT_ROOT / "data" / "geojson" / "voronoi_zones.geojson"
    intersections_path = PROJECT_ROOT / "data" / "geojson" / "intersections.json"

    zones_gdf = gpd.read_file(zones_path)
    if "index" not in zones_gdf.columns:
        zones_gdf["index"] = zones_gdf.index.astype(int)
    if "camera_id" not in zones_gdf.columns:
        zones_gdf["camera_id"] = zones_gdf["id"]
    if "camera_name" not in zones_gdf.columns:
        zones_gdf["camera_name"] = zones_gdf["name"]

    zones_gdf, transformer = project_zones_for_distance(zones_gdf)
    neighbors = find_neighbors(zones_gdf)

    camera_payloads = json.loads(stress_scores_path.read_text()).get("camera_stress", {})
    camera_stress, _, summary = resolve_camera_stress_map(camera_payloads)

    pathfinder = LearnedHeuristicPathfinder(
        stress_scores_path=stress_scores_path,
        intersections_path=intersections_path,
        use_regularization=False,
    )

    model = IntersectionStressModel.from_voronoi_zones(
        graph=pathfinder.graph,
        zones_gdf=zones_gdf,
        neighbors=neighbors,
        camera_stress=camera_stress,
        neighbor_weight=0.5,
        second_order_weight=0.25,
        transformer=transformer,
        stress_source_key=summary.get("chosen_key"),
    )

    pathfinder.intersection_stress = model.intersection_stress
    result = pathfinder.find_path(85, 50)

    if result.nodes != trace["route_nodes"]:
        print("FAIL: route nodes mismatch")
        return 1

    edge_trace = trace["edge_trace"]
    tol = 1e-9
    for idx, edge in enumerate(edge_trace):
        u = edge["edge_u"]
        v = edge["edge_v"]
        edge_stress = 0.5 * (model.get_scalar(u) + model.get_scalar(v))
        if abs(edge_stress - edge["edge_stress"]) > tol:
            print(f"FAIL: edge stress mismatch at index {idx}")
            print(edge_stress, edge["edge_stress"])
            return 1

    print("PASS: intersection stress parity matches activation trace")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
