# Limitations

- Confidence reuse is only admissible when Phase 2 compatibility conditions hold and remains tied to decision identity labels and identity persistence regions from fig2 and fig3.
- Trace coverage is limited to the sweep points recorded in fig2 and the boundary flags recorded in fig4. No new parameter values are introduced.
- Observables are limited to equivalence_policy_reference, path_nodes_sequence, decision_identity_label, identity_persistence_region, route_changed_flag, and edge_order_changed_flag as defined in observables_map.yaml.
- Conditions without mapped observables are not resolved in the trace set and require separate review.
- This phase does not introduce calibration, logging, or evaluation procedures. If a reviewer interprets reuse checks as any of these, treat it as a misinterpretation to be corrected.
