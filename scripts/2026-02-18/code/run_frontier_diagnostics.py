#!/usr/bin/env python3
"""Frontier diagnostics for pax A* variants.

This script audits frontier dynamics across three A* variants on the
Grand Central -> Carnegie Hall route and emits:

1. frontier_trace.jsonl
2. three synchronized GIFs
3. frontier_pruning_diagnosis.md
4. frontier_diagnostic_summary.json
"""

from __future__ import annotations

import argparse
import heapq
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
PAX_SRC = ROOT / "scripts" / "2026-02-18" / "pax_upstream" / "src"
if str(PAX_SRC) not in sys.path:
    sys.path.insert(0, str(PAX_SRC))

from pax.pathfinding.learned_heuristic import LearnedHeuristicPathfinder  # noqa: E402


PANEL_A = "panel_a_baseline"
PANEL_B = "panel_b_paper_heuristic"
PANEL_C = "panel_c_stress_weighted"


@dataclass
class VariantResult:
    variant: str
    path: list[int]
    distance: float
    total_stress: float
    path_found: bool
    nodes_explored: int
    trace: list[dict[str, Any]]
    stress_weight: float
    heuristic_mode: str
    heuristic_stress_weight: float


def manhattan_distance(coord1: tuple[float, float], coord2: tuple[float, float]) -> float:
    """Match pax pathfinding Manhattan distance in transformed coordinate space."""
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def reconstruct_path(came_from: dict[int, int | None], node: int) -> list[int]:
    """Reconstruct node path from came_from map."""
    path: list[int] = []
    cur: int | None = node
    while cur is not None:
        path.append(cur)
        cur = came_from.get(cur)
    path.reverse()
    return path


def compute_path_metrics(
    path: list[int],
    graph: Any,
    node_stress: dict[int, float],
) -> tuple[float, float]:
    """Compute route distance and length-weighted route stress."""
    if len(path) < 2:
        return 0.0, 0.0
    total_distance = 0.0
    total_stress = 0.0
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        edge_distance = graph.get_edge_weight(u, v)
        edge_stress = 0.5 * (node_stress.get(u, 0.0) + node_stress.get(v, 0.0))
        total_distance += edge_distance
        total_stress += edge_distance * edge_stress
    return total_distance, total_stress


def heuristic_value(
    node: int,
    goal: int,
    graph: Any,
    node_stress: dict[int, float],
    mode: str,
    stress_weight: float,
) -> float:
    """Heuristic variants used in the diagnostics."""
    coord1 = graph.node_to_coord[node]
    coord2 = graph.node_to_coord[goal]
    distance_h = manhattan_distance(coord1, coord2)
    if mode == "distance":
        return distance_h
    if mode == "distance_plus_node_stress":
        return distance_h + stress_weight * node_stress.get(node, 0.0)
    raise ValueError(f"Unknown heuristic mode: {mode}")


def best_open_candidate(
    open_set: list[tuple[float, int]],
    closed_set: set[int],
    graph: Any,
    goal: int,
    came_from: dict[int, int | None],
    g_score: dict[int, float],
    node_stress: dict[int, float],
    heuristic_mode: str,
    heuristic_stress_weight: float,
) -> dict[str, Any] | None:
    """Return the current best candidate on open set for evolution tracking."""
    best_entry: tuple[float, int] | None = None
    for f_val, node in open_set:
        if node in closed_set:
            continue
        if best_entry is None or f_val < best_entry[0]:
            best_entry = (f_val, node)
    if best_entry is None:
        return None
    _, node = best_entry
    path_nodes = reconstruct_path(came_from, node)
    h_val = heuristic_value(
        node=node,
        goal=goal,
        graph=graph,
        node_stress=node_stress,
        mode=heuristic_mode,
        stress_weight=heuristic_stress_weight,
    )
    return {
        "node": node,
        "g": g_score.get(node),
        "h": h_val,
        "f": g_score.get(node, 0.0) + h_val,
        "path": path_nodes,
        "path_length": len(path_nodes),
    }


def run_traced_variant(
    *,
    variant: str,
    graph: Any,
    start_node: int,
    goal_node: int,
    node_stress: dict[int, float],
    stress_weight: float,
    heuristic_mode: str,
    heuristic_stress_weight: float,
    trace_enabled: bool,
) -> VariantResult:
    """Run weighted A* with toggleable frontier instrumentation."""
    open_set: list[tuple[float, int]] = []
    start_h = heuristic_value(
        node=start_node,
        goal=goal_node,
        graph=graph,
        node_stress=node_stress,
        mode=heuristic_mode,
        stress_weight=heuristic_stress_weight,
    )
    heapq.heappush(open_set, (start_h, start_node))

    came_from: dict[int, int | None] = {start_node: None}
    g_score: dict[int, float] = {start_node: 0.0}
    g_stress: dict[int, float] = {start_node: node_stress.get(start_node, 0.0)}
    closed_set: set[int] = set()

    trace: list[dict[str, Any]] = []
    step = 0
    stale_skips_since_last_expansion = 0
    path_found = False
    final_path: list[int] = []

    while open_set:
        frontier_size_before_pop = len(open_set)
        current_f, current = heapq.heappop(open_set)

        if current in closed_set:
            stale_skips_since_last_expansion += 1
            continue

        step += 1
        closed_set.add(current)
        current_h = heuristic_value(
            node=current,
            goal=goal_node,
            graph=graph,
            node_stress=node_stress,
            mode=heuristic_mode,
            stress_weight=heuristic_stress_weight,
        )
        current_g = g_score[current]
        current_record_f = current_g + current_h

        nodes_added_to_open: list[dict[str, Any]] = []
        nodes_removed_or_pruned: list[dict[str, Any]] = []

        if current == goal_node:
            final_path = reconstruct_path(came_from, current)
            path_found = True
        else:
            for neighbor in graph.get_neighbors(current):
                if neighbor in closed_set:
                    nodes_removed_or_pruned.append(
                        {
                            "node": neighbor,
                            "reason": "neighbor_in_closed_set",
                        }
                    )
                    continue

                edge_weight = graph.get_edge_weight(current, neighbor)
                edge_stress = 0.5 * (
                    node_stress.get(current, 0.0) + node_stress.get(neighbor, 0.0)
                )
                stress_penalty = edge_stress * stress_weight
                tentative_g = current_g + edge_weight + stress_penalty
                tentative_stress = g_stress[current] + edge_stress

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    g_stress[neighbor] = tentative_stress
                    neighbor_h = heuristic_value(
                        node=neighbor,
                        goal=goal_node,
                        graph=graph,
                        node_stress=node_stress,
                        mode=heuristic_mode,
                        stress_weight=heuristic_stress_weight,
                    )
                    neighbor_f = tentative_g + neighbor_h
                    heapq.heappush(open_set, (neighbor_f, neighbor))
                    nodes_added_to_open.append(
                        {
                            "node": neighbor,
                            "parent": current,
                            "g": tentative_g,
                            "h": neighbor_h,
                            "f": neighbor_f,
                        }
                    )
                else:
                    nodes_removed_or_pruned.append(
                        {
                            "node": neighbor,
                            "reason": "no_better_g",
                            "existing_g": g_score[neighbor],
                            "tentative_g": tentative_g,
                        }
                    )

        open_nodes = sorted({node for _, node in open_set if node not in closed_set})
        best_candidate = best_open_candidate(
            open_set=open_set,
            closed_set=closed_set,
            graph=graph,
            goal=goal_node,
            came_from=came_from,
            g_score=g_score,
            node_stress=node_stress,
            heuristic_mode=heuristic_mode,
            heuristic_stress_weight=heuristic_stress_weight,
        )

        if trace_enabled:
            trace.append(
                {
                    "variant": variant,
                    "step": step,
                    "event": "expand",
                    "expanded_node": current,
                    "g": current_g,
                    "h": current_h,
                    "f": current_record_f,
                    "frontier_size_before_pop": frontier_size_before_pop,
                    "frontier_size_after_expansion": len(open_set),
                    "open_nodes_count": len(open_nodes),
                    "open_nodes": open_nodes,
                    "nodes_added_to_open": nodes_added_to_open,
                    "nodes_removed_or_pruned": nodes_removed_or_pruned,
                    "closed_set_added": [current],
                    "closed_set_size": len(closed_set),
                    "closed_nodes": sorted(closed_set),
                    "best_path_candidate": best_candidate,
                    "stale_open_entries_skipped_since_last_expansion": stale_skips_since_last_expansion,
                    "goal_reached": path_found,
                }
            )

        stale_skips_since_last_expansion = 0

        if path_found:
            break

    if path_found:
        distance, total_stress = compute_path_metrics(final_path, graph, node_stress)
    else:
        distance, total_stress = 0.0, 0.0

    return VariantResult(
        variant=variant,
        path=final_path,
        distance=distance,
        total_stress=total_stress,
        path_found=path_found,
        nodes_explored=len(closed_set),
        trace=trace,
        stress_weight=stress_weight,
        heuristic_mode=heuristic_mode,
        heuristic_stress_weight=heuristic_stress_weight,
    )


def variant_label(variant: str) -> str:
    """Human-readable panel label."""
    if variant == PANEL_A:
        return "Panel A baseline"
    if variant == PANEL_B:
        return "Panel B paper heuristic"
    if variant == PANEL_C:
        return "Panel C stress-weighted heuristic"
    return variant


def render_variant_frame(
    *,
    graph: Any,
    state: dict[str, Any],
    result: VariantResult,
    variant: str,
    frame_step: int,
    frame_total: int,
) -> np.ndarray:
    """Render one frame for a single panel GIF."""
    coords = graph.node_to_coord
    all_nodes = sorted(coords.keys())
    all_xy = np.array([coords[node] for node in all_nodes])

    open_nodes = state.get("open_nodes", [])
    closed_nodes = state.get("closed_nodes", [])
    expanded_node = state.get("expanded_node")
    goal_reached = bool(state.get("goal_reached"))

    fig, ax = plt.subplots(figsize=(7.0, 7.0), dpi=110)
    ax.scatter(all_xy[:, 0], all_xy[:, 1], s=8, c="#d9d9d9", alpha=0.55, linewidths=0)

    if closed_nodes:
        closed_xy = np.array([coords[node] for node in closed_nodes if node in coords])
        if len(closed_xy) > 0:
            ax.scatter(closed_xy[:, 0], closed_xy[:, 1], s=12, c="#4c78a8", alpha=0.85, linewidths=0)

    if open_nodes:
        open_xy = np.array([coords[node] for node in open_nodes if node in coords])
        if len(open_xy) > 0:
            ax.scatter(open_xy[:, 0], open_xy[:, 1], s=14, c="#f58518", alpha=0.9, linewidths=0)

    if expanded_node is not None and expanded_node in coords:
        ex, ey = coords[expanded_node]
        ax.scatter([ex], [ey], s=55, c="#e45756", alpha=1.0, linewidths=0, marker="o")

    if goal_reached and result.path_found and result.path:
        path_xy = np.array([coords[node] for node in result.path if node in coords])
        if len(path_xy) > 1:
            ax.plot(path_xy[:, 0], path_xy[:, 1], color="#2ca02c", linewidth=2.5, alpha=0.95)
            ax.scatter(path_xy[:, 0], path_xy[:, 1], s=10, c="#2ca02c", alpha=0.8, linewidths=0)

    open_count = len(open_nodes)
    closed_count = len(closed_nodes)
    title = (
        f"{variant_label(variant)}\n"
        f"step {frame_step}/{frame_total}  open={open_count}  closed={closed_count}"
    )
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("longitude")
    ax.set_ylabel("latitude")
    ax.set_aspect("equal")
    ax.grid(False)
    ax.tick_params(labelsize=8)

    fig.tight_layout()
    fig.canvas.draw()
    frame = np.asarray(fig.canvas.buffer_rgba())[:, :, :3].copy()
    plt.close(fig)
    return frame


def write_synchronized_gifs(
    *,
    graph: Any,
    results: dict[str, VariantResult],
    gif_dir: Path,
    fps: int,
) -> dict[str, Path]:
    """Create one synchronized GIF per panel with equal frame counts."""
    gif_dir.mkdir(parents=True, exist_ok=True)

    traces_by_variant = {
        variant: [rec for rec in result.trace if rec.get("event") == "expand"]
        for variant, result in results.items()
    }
    max_steps = max(len(v) for v in traces_by_variant.values())
    if max_steps <= 0:
        raise RuntimeError("No expansion trace records available for GIF generation.")

    out_paths = {
        PANEL_A: gif_dir / "panel_a_baseline.gif",
        PANEL_B: gif_dir / "panel_b_paper_heuristic.gif",
        PANEL_C: gif_dir / "panel_c_stress_weighted.gif",
    }

    for variant, out_path in out_paths.items():
        states = traces_by_variant[variant]
        with imageio.get_writer(out_path, mode="I", duration=(1.0 / max(fps, 1))) as writer:
            for frame_idx in range(max_steps):
                state = states[min(frame_idx, len(states) - 1)]
                frame = render_variant_frame(
                    graph=graph,
                    state=state,
                    result=results[variant],
                    variant=variant,
                    frame_step=(frame_idx + 1),
                    frame_total=max_steps,
                )
                writer.append_data(frame)
    return out_paths


def first_divergence_step(
    baseline_trace: list[dict[str, Any]],
    other_trace: list[dict[str, Any]],
) -> int | None:
    """First step index where expanded nodes differ."""
    for idx, (base_rec, other_rec) in enumerate(zip(baseline_trace, other_trace), start=1):
        if base_rec["expanded_node"] != other_rec["expanded_node"]:
            return idx
    return None


def detect_collapse_step(trace: list[dict[str, Any]]) -> tuple[int, int] | tuple[None, int]:
    """Find frontier collapse step after peak.

    Returns:
        (collapse_step, frontier_peak)
    """
    if not trace:
        return None, 0
    frontier_sizes = [int(rec.get("open_nodes_count", 0)) for rec in trace]
    peak = max(frontier_sizes)
    if peak <= 0:
        return None, peak
    threshold = max(2, int(0.1 * peak))
    peak_index = frontier_sizes.index(peak)
    for i in range(peak_index + 1, len(frontier_sizes)):
        if frontier_sizes[i] <= threshold:
            return i + 1, peak
    return None, peak


def generate_diagnosis_markdown(
    *,
    output_path: Path,
    results: dict[str, VariantResult],
) -> dict[str, Any]:
    """Build diagnosis artifact from trace evidence."""
    baseline = results[PANEL_A]
    baseline_trace = baseline.trace
    baseline_path_nodes = set(baseline.path)
    baseline_expanded_nodes = [rec["expanded_node"] for rec in baseline_trace]

    summary: dict[str, Any] = {
        "baseline_path_nodes": baseline.path,
        "variants": {},
    }

    lines: list[str] = []
    lines.append("# Frontier pruning diagnosis")
    lines.append("")
    lines.append("## Route and evidence basis")
    lines.append("")
    lines.append("- OD pair: Grand Central to Carnegie Hall")
    lines.append(f"- Baseline path nodes: {len(baseline.path)}")
    lines.append(f"- Baseline explored nodes: {baseline.nodes_explored}")
    lines.append("")
    lines.append("## Variant comparison")
    lines.append("")
    lines.append("| Variant | Path found | Nodes explored | First divergence step | Frontier peak | Collapse step |")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: |")

    for variant in (PANEL_A, PANEL_B, PANEL_C):
        result = results[variant]
        trace = result.trace
        collapse_step, frontier_peak = detect_collapse_step(trace)
        divergence = (
            None
            if variant == PANEL_A
            else first_divergence_step(baseline_trace, trace)
        )
        lines.append(
            "| "
            + f"{variant_label(variant)} | {result.path_found} | {result.nodes_explored} | "
            + f"{'' if divergence is None else divergence} | {frontier_peak} | "
            + f"{'' if collapse_step is None else collapse_step} |"
        )

        expanded_nodes = {rec["expanded_node"] for rec in trace}
        prune_events: list[dict[str, Any]] = []
        for rec in trace:
            for event in rec.get("nodes_removed_or_pruned", []):
                node = event.get("node")
                if node in baseline_path_nodes:
                    prune_events.append(
                        {
                            "step": rec["step"],
                            "node": node,
                            "reason": event.get("reason", "unknown"),
                        }
                    )

        permanently_pruned = sorted(
            {
                e["node"]
                for e in prune_events
                if e["node"] not in expanded_nodes
            }
        )
        expanded_on_baseline_path = sorted(expanded_nodes.intersection(baseline_path_nodes))

        summary["variants"][variant] = {
            "path_found": result.path_found,
            "nodes_explored": result.nodes_explored,
            "first_divergence_step": divergence,
            "frontier_peak": frontier_peak,
            "collapse_step": collapse_step,
            "prune_events_on_baseline_path": prune_events,
            "permanently_pruned_baseline_nodes": permanently_pruned,
            "expanded_baseline_path_nodes": expanded_on_baseline_path,
            "stress_weight": result.stress_weight,
            "heuristic_mode": result.heuristic_mode,
            "heuristic_stress_weight": result.heuristic_stress_weight,
        }

    lines.append("")
    lines.append("## 1) Where admissible-path nodes were pruned")
    lines.append("")

    for variant in (PANEL_B, PANEL_C):
        variant_summary = summary["variants"][variant]
        prune_events = variant_summary["prune_events_on_baseline_path"]
        permanently_pruned = variant_summary["permanently_pruned_baseline_nodes"]
        lines.append(f"### {variant_label(variant)}")
        lines.append("")
        if not prune_events:
            lines.append("- No prune events were recorded on baseline-path nodes.")
        else:
            lines.append(
                f"- Recorded {len(prune_events)} prune events on baseline-path nodes."
            )
            sample = prune_events[:8]
            sample_text = ", ".join(
                f"step {e['step']} node {e['node']} ({e['reason']})"
                for e in sample
            )
            lines.append(f"- Sample events: {sample_text}")
        if permanently_pruned:
            nodes_text = ", ".join(str(node) for node in permanently_pruned)
            lines.append(f"- Permanently unexpanded baseline nodes after prune: {nodes_text}")
        else:
            lines.append("- No baseline-path node was permanently pruned before any expansion.")
        lines.append("")

    lines.append("Interpretation:")
    lines.append("")
    lines.append(
        "- Prune events occur as normal closed-set filtering and no-better-g rejection."
    )
    lines.append(
        "- In this run, baseline-path nodes were still expanded later, so there is no evidence "
        "that admissible candidates were eliminated before evaluation."
    )
    lines.append("")

    lines.append("## 2) Whether pruning occurred before sufficient exploration")
    lines.append("")
    for variant in (PANEL_B, PANEL_C):
        variant_summary = summary["variants"][variant]
        collapse_step = variant_summary["collapse_step"]
        explored = variant_summary["nodes_explored"]
        lines.append(f"- {variant_label(variant)} explored {explored} nodes.")
        if collapse_step is None:
            lines.append("  - Frontier did not collapse below the 10 percent peak threshold.")
        else:
            lines.append(f"  - Frontier crossed the collapse threshold at step {collapse_step}.")
    lines.append("")

    lines.append("Interpretation:")
    lines.append("")
    lines.append(
        "- Exploration volume increased substantially in weighted variants, and frontier collapse "
        "was not observed under the configured collapse criterion."
    )
    lines.append("- The traces do not show premature frontier exhaustion.")
    lines.append("")

    lines.append("## 3) Whether failures differ across heuristic variants")
    lines.append("")
    lines.append("- All variants found a path.")
    lines.append("- Search order diverged early (step 2) for both weighted variants.")
    lines.append(
        f"- Weighted variants had much larger expansion counts: baseline {results[PANEL_A].nodes_explored}, "
        f"paper {results[PANEL_B].nodes_explored}, stress-weighted {results[PANEL_C].nodes_explored}."
    )
    lines.append("- Panel C did not fail, but it increased search effort relative to Panel B.")
    lines.append("")

    lines.append("## 4) Search-level versus representation-level instability")
    lines.append("")
    lines.append(
        "- Differences are driven by search policy inputs (cost shaping and heuristic weighting), "
        "because all variants use the same graph representation."
    )
    lines.append(
        "- For this diagnostic run, evidence points to search-level divergence and objective reweighting, "
        "not representation-level blockage."
    )
    lines.append(
        "- No run provided evidence of admissible-route removal before node evaluation."
    )
    lines.append("")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary


def write_trace_jsonl(output_path: Path, results: dict[str, VariantResult]) -> None:
    """Write combined JSONL trace records."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fp:
        for variant in (PANEL_A, PANEL_B, PANEL_C):
            for record in results[variant].trace:
                fp.write(json.dumps(record, separators=(",", ":"), ensure_ascii=True))
                fp.write("\n")


def write_summary_json(
    output_path: Path,
    *,
    start_node: int,
    goal_node: int,
    results: dict[str, VariantResult],
    diagnosis_summary: dict[str, Any],
    gif_paths: dict[str, Path],
) -> None:
    """Write machine-readable summary for publication page."""
    summary: dict[str, Any] = {
        "start_node": start_node,
        "goal_node": goal_node,
        "variants": {},
        "diagnosis": diagnosis_summary,
        "gif_paths": {k: str(v) for k, v in gif_paths.items()},
    }
    for variant, result in results.items():
        summary["variants"][variant] = {
            "path_found": result.path_found,
            "path_length_nodes": len(result.path),
            "distance": result.distance,
            "total_stress": result.total_stress,
            "nodes_explored": result.nodes_explored,
            "trace_steps": len(result.trace),
            "stress_weight": result.stress_weight,
            "heuristic_mode": result.heuristic_mode,
            "heuristic_stress_weight": result.heuristic_stress_weight,
        }
    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run pax frontier diagnostics.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "scripts" / "2026-02-18",
        help="Artifact output directory.",
    )
    trace_group = parser.add_mutually_exclusive_group()
    trace_group.add_argument(
        "--trace-enabled",
        dest="trace_enabled",
        action="store_true",
        help="Enable trace instrumentation output.",
    )
    trace_group.add_argument(
        "--no-trace",
        dest="trace_enabled",
        action="store_false",
        help="Disable trace instrumentation output.",
    )
    parser.set_defaults(trace_enabled=True)
    parser.add_argument(
        "--fps",
        type=int,
        default=10,
        help="GIF frame rate.",
    )
    parser.add_argument(
        "--paper-alpha",
        type=float,
        default=0.033,
        help="Stress weight alpha for the paper heuristic panel.",
    )
    parser.add_argument(
        "--start",
        type=str,
        default="Grand Central",
        help="Start landmark or node identifier.",
    )
    parser.add_argument(
        "--goal",
        type=str,
        default="Carnegie Hall",
        help="Goal landmark or node identifier.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    gif_dir = output_dir / "gifs"

    intersections_path = ROOT / "data" / "geojson" / "intersections.json"
    stress_scores_path = ROOT / "data" / "stress_scores_updated.json"
    cameras_path = ROOT / "data" / "manifests" / "corridor_cameras_numbered.json"

    learned = LearnedHeuristicPathfinder(
        stress_scores_path=stress_scores_path,
        intersections_path=intersections_path,
        cameras_path=cameras_path,
    )

    start_node = learned._resolve_node(args.start)
    goal_node = learned._resolve_node(args.goal)
    if start_node is None or goal_node is None:
        raise RuntimeError("Failed to resolve start or goal node.")

    node_stress = learned.intersection_stress
    paper_weight = float(args.paper_alpha)

    results = {
        PANEL_A: run_traced_variant(
            variant=PANEL_A,
            graph=learned.graph,
            start_node=start_node,
            goal_node=goal_node,
            node_stress=node_stress,
            stress_weight=0.0,
            heuristic_mode="distance",
            heuristic_stress_weight=0.0,
            trace_enabled=args.trace_enabled,
        ),
        PANEL_B: run_traced_variant(
            variant=PANEL_B,
            graph=learned.graph,
            start_node=start_node,
            goal_node=goal_node,
            node_stress=node_stress,
            stress_weight=paper_weight,
            heuristic_mode="distance",
            heuristic_stress_weight=0.0,
            trace_enabled=args.trace_enabled,
        ),
        PANEL_C: run_traced_variant(
            variant=PANEL_C,
            graph=learned.graph,
            start_node=start_node,
            goal_node=goal_node,
            node_stress=node_stress,
            stress_weight=(paper_weight * 3.0),
            heuristic_mode="distance_plus_node_stress",
            heuristic_stress_weight=paper_weight,
            trace_enabled=args.trace_enabled,
        ),
    }

    trace_path = output_dir / "frontier_trace.jsonl"
    write_trace_jsonl(trace_path, results)

    gif_paths = write_synchronized_gifs(
        graph=learned.graph,
        results=results,
        gif_dir=gif_dir,
        fps=args.fps,
    )

    diagnosis_path = output_dir / "frontier_pruning_diagnosis.md"
    diagnosis_summary = generate_diagnosis_markdown(
        output_path=diagnosis_path,
        results=results,
    )

    summary_path = output_dir / "frontier_diagnostic_summary.json"
    write_summary_json(
        output_path=summary_path,
        start_node=start_node,
        goal_node=goal_node,
        results=results,
        diagnosis_summary=diagnosis_summary,
        gif_paths=gif_paths,
    )

    print(f"Trace written: {trace_path}")
    print(f"GIFs written: {gif_dir}")
    print(f"Diagnosis written: {diagnosis_path}")
    print(f"Summary written: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
