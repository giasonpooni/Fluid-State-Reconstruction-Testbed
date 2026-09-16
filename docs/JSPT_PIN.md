# JSPT pin

A2-A5 live in JSPT. This repository wraps types; it does not own the law.

Pinned SHA: `c0a01c1a27f10b099ac200c7e83b0f03187ee4d2`

Live call site: `set_lcm.bridge.jspt.map_covariance` → `sensitivity.push_covariance`.
`AffineCoordinates._map_covariance` must use that function (no local `T @ P @ T.T`).
See `tests/test_jspt_chart.py`.

Default CI stays numpy-only so a JSPT axiom change cannot silently rewrite reports.
Install the extra to compare.

Keep `GaussianState`, masks, Joseph, and declaration here.
CSE / Lyapunov / geodesic take this same SHA from commit one.
