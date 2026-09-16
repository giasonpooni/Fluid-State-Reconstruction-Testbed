# JSPT pin

JSPT owns the chart and first-order covariance laws. This repository wraps
`GaussianState` and must not fork `T P Tᵀ` / `T F T⁻¹`.

Pinned SHA (laws, not floating main):

`d570b2cf6553c80217f78a2ada62b5dc456c7469`

https://github.com/giasonpooni/Jacobian-Sensitivity-Propagation-Testbed/commit/d570b2cf6553c80217f78a2ada62b5dc456c7469

Optional extra when the adapter is wired:

```toml
jspt = [
  "jacobian-sensitivity-propagation-testbed @ git+https://github.com/giasonpooni/Jacobian-Sensitivity-Propagation-Testbed.git@d570b2cf6553c80217f78a2ada62b5dc456c7469",
]
```

Do not copy `coordinates.py` from JSPT. Bump the SHA only after
`tests/test_jspt_chart_contract.py` and JSPT `tests/contracts/test_chart_law.py`
both pass on the same two-tank fixture.
