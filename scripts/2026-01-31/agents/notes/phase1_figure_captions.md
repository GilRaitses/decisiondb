# Phase 1 Draft Figure Captions

Figure 1. Canonical decision-valued mapping schematic. A fixed snapshot is encoded into a representation family. Each representation is executed by a fixed engine and yields raw output. An equivalence policy extracts a discrete decision identity from the raw output. The decision map links representation identifiers, engine runs, and decision identities.

Figure 2. Primary representational sweep for one snapshot and engine. Each variant corresponds to a weight setting recorded in the weight variation results. Decision identity is defined by the route node sequence in each variant. Identical identities use the same label.

Figure 3. Identity persistence regions derived from Figure 2. Consecutive variants with identical decision identity labels are shown as a single region, indicating persistence under the tested weight changes.

Figure 4. Boundary and fracture localization derived from Figure 2. Transitions where route_changed or edge_order_changed is true are marked as boundaries, with baseline and perturbed weight values listed.

Figure 5. Reproducibility replay verification. The replay verification logs show recomputed policy identifier, payload hash, and decision identifier matching the persisted manifest, and table counts remain unchanged.
