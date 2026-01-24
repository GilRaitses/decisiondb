FIGURE_CHECKLIST.md

DecisionDB Figure Compliance Checklist

This checklist defines mandatory requirements for all figures included in DecisionDB repositories, related manuscripts, presentations, and documentation.

A figure that fails any required item must not be included.
This checklist is normative, not advisory.

⸻

1. Figure Purpose Declaration

Every figure must explicitly answer one of the following questions:
	•	Which discrete decision identity is produced under each representation configuration?
	•	Where is decision identity constant across representation space?
	•	Where does decision identity change as representation varies?

If the figure does not directly answer one of these questions, it is out of scope.

⸻

2. Data and Engine Constraints

Confirm all of the following:
	•	Raw data is fixed across the entire figure.
	•	The decision engine or solver is fixed across the entire figure.
	•	Only representation parameters vary.

If any of these conditions are not met, the figure must be rejected.

⸻

3. Axes Validation

For every axis in the figure:
	•	The axis corresponds to a concrete representation parameter.
	•	The parameter exists as a configurable key in code or configuration files.
	•	The axis label matches the exact parameter name or a documented alias.

Disallowed axes include:
	•	abstract parameters
	•	symbolic variables
	•	inferred or latent quantities
	•	biologically or physically interpreted variables

If an axis cannot be instantiated programmatically, it must not appear.

⸻

4. Dimensionality Rules

Allowed:
	•	1D plots showing decision identity vs representation parameter
	•	2D grids or matrices of representation parameters
	•	Small multiples of 2D plots

Disallowed:
	•	3D surfaces
	•	continuous manifolds
	•	interpolated volumes
	•	projections that imply continuity

Representation space is treated as discrete unless explicitly enumerated.

⸻

5. Encoding of Decision Identity

Decision identity must be encoded categorically.

Allowed encodings:
	•	flat colors
	•	discrete textures or patterns
	•	explicit labels (e.g. D_01, D_07)

Disallowed encodings:
	•	gradients
	•	heatmaps
	•	opacity ramps
	•	colorbars representing magnitude
	•	interpolated shading

Decision identity is not a scalar quantity.

⸻

6. Boundary Representation

Boundaries must satisfy all of the following:
	•	Boundaries indicate adjacency changes between configurations.
	•	Boundaries arise from observed changes in discrete output.
	•	Boundaries are visually discrete.

Disallowed boundary features:
	•	smoothing
	•	curve fitting
	•	threshold lines
	•	arrows implying flow or direction

Approved boundary labels:
	•	decision change boundary
	•	identity boundary

⸻

7. Caption Compliance

Every figure caption must include:
	•	A statement that decision identity is discrete.
	•	A statement that variation is due to representation choice.
	•	A statement that data and engine are held fixed.

Captions must not include:
	•	physical metaphors
	•	biological interpretation
	•	learning or intelligence claims
	•	theoretical framing

Captions must be interpretable by a reader outside the application domain.

⸻

8. Terminology Scan

Before inclusion, verify that the figure and caption contain none of the following terms:
	•	phase
	•	critical
	•	transition
	•	bifurcation
	•	attractor
	•	emergent
	•	intelligence
	•	dynamics (unless referring to recorded time series)
	•	regime (unless explicitly “decision regime”)

If any appear, the figure must be corrected or rejected.

⸻

9. Visual Neutrality

Figures must avoid implying causality or mechanism.

Disallowed visual elements:
	•	arrows suggesting influence
	•	gradients suggesting intensity
	•	layouts implying optimization
	•	annotations implying explanation

Figures are diagnostic, not explanatory.

⸻

10. Reproducibility Check

For each figure, the following must exist:
	•	A script or notebook that generates the figure.
	•	A configuration file enumerating representation parameters.
	•	A logged mapping from representation configuration to decision identity.

If the figure cannot be regenerated from logged data, it is invalid.

⸻

11. Final Acceptance Criteria

A figure is acceptable only if:
	•	It conforms to STYLE_GUIDE.md.
	•	It passes every item in this checklist.
	•	Its meaning can be stated entirely in terms of f : R → D.

If not, it does not belong in DecisionDB.