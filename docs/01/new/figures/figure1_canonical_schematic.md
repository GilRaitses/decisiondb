# Figure 1: Canonical Decision-Valued Mapping Schematic

## Decision identity definition
Decision identity is a discrete label extracted from engine output by an equivalence policy. Two outputs share the same identity if and only if the policy maps them to the same label.

## Representation axes
This figure is a schematic diagram. No representation parameter axes are plotted. The diagram shows the pipeline from snapshot to representation to engine to equivalence policy to decision identity.

## Equivalence rule
The equivalence policy shown in the schematic applies a declared rule to reduce raw engine output to a discrete identity. In the demonstrated instance, the policy uses SHA-256 equality over canonicalized route node sequences.

## Stability criterion
Not applicable to this schematic. Stability (persistence) is observable only in Figures 2 and 3, which evaluate the map at multiple representation parameter values.

## Sampling method
Not applicable. This figure is a conceptual diagram, not an empirical result.

## Non-claims disclaimer
This figure makes no performance claims, optimization claims, or learning claims. It illustrates the structural pipeline from representation to decision identity under fixed snapshot and engine.
