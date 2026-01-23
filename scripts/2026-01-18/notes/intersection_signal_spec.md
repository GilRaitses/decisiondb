# Intersection Signal Specification (Pre-Refactor)

Purpose: Define, in precise and operational terms, what it means for stress to be owned at the
intersection layer. This is a specification only.

## Definition: intersection signal
An intersection signal is the locally owned stress representation attached to a graph node
(intersection) that is used to compute routing costs on adjacent edges. It is the first stress
artifact that is indexed by intersection ID rather than by camera or zone.

## What an intersection owns that zones do not
- A stable node identifier in the routing graph.
- A localized stress representation aligned to a unique spatial node.
- A record of how multiple upstream camera or zone inputs were combined for that node.

## What it aggregates vs preserves
- Aggregates: camera or zone stress inputs that contribute to the node.
- Preserves: node identity, spatial position, and the combination rule used to form the signal.

## Scalar vs structured quantities
- Scalar: the primary stress score used for routing costs.
- Structured: optional metadata (e.g., source keys used, fallback flags, contributing sources).

## What is passed downstream to routing
- A scalar stress value per intersection.
- Optional metadata used for audit or traceability, not for route selection.

## What is explicitly not decided at the intersection level
- Route selection decisions.
- Global policy about tradeoffs across routes.
- Block-level aggregation (explicitly deferred).

## Prompts
### Is an intersection signal one value or a bundle of values
It is a bundle with a required scalar stress value plus optional metadata. The routing layer consumes
the scalar only.

### Which components are invariant under aggregation
Node identity and spatial location are invariant. The aggregation rule must be recorded to make
changes traceable.

### Which components are expected to change under perturbation
The scalar stress value and any metadata tied to aggregation inputs may change when coefficients or
inputs change.

### Alignment with Chapter 0 maps between representations
The intersection signal is a representation produced by a map from camera- or zone-level inputs to
intersection-level outputs. This describes a change of representation without asserting equivalence.

## Scope notes
- This specification stands without block-level aggregation.
- It defines ownership and data shape only; no implementation details are included.
