# JSPT pin

A2-A5 live in JSPT. This repository wraps types; it does not own the law.

Pinned SHA: `c0a01c1a27f10b099ac200c7e83b0f03187ee4d2`

```toml
[project.optional-dependencies]
jspt = [
  "jacobian-sensitivity-propagation-testbed @ git+https://github.com/giasonpooni/Jacobian-Sensitivity-Propagation-Testbed.git@c0a01c1a27f10b099ac200c7e83b0f03187ee4d2",
]
```

Bumping the pin is a reviewed act: run `tests/test_coordinates.py` and
`tests/test_jspt_chart_contract.py`, then move the SHA. Do not copy
`coordinates.py` from JSPT.

Default CI stays numpy-only (`uv run --frozen`) so a JSPT axiom change
cannot silently rewrite NOAA reports. Install the extra to compare:

```bash
uv run --python 3.13 --extra jspt --dev pytest -q tests/test_jspt_chart_contract.py tests/test_jspt_adapter.py
```

Week-2, after that extra is green: `AffineCoordinates` becomes a thin
adapter over `sensitivity.AffineCoordinates` / `push_covariance` /
`transform_plant`. Keep `GaussianState`, masks, Joseph, and declaration.

**Same pull request, not a follow-up:** delete the local `T F T^{-1}` and
`T P T^T` algebra when the adapter lands. Leaving both copies will drift.

CSE / Lyapunov / geodesic repos take this same SHA from commit one.
Do not grow a second IFC or OpenUSD stack here.
