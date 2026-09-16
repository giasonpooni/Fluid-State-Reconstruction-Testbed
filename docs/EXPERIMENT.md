# Experiment next to the other tools

FSRT is its own experiment. It does not feed Beam-B1 and it does not
live in an SP1 guest.

## Run this repo

```bash
git clone https://github.com/giasonpooni/Fluid-State-Reconstruction-Testbed.git
cd Fluid-State-Reconstruction-Testbed
uv run --frozen --python 3.13 python examples/quickstart.py
```

That writes a two-tank reconciliation report. It is not a millimetre and
it is not `YieldStrengthMPa`.

## What this repo does not do

- Import GAT or `flat_torus`.
- Emit an `rci-evidence-commitment-v1` or `torus-report-commitment-v1`.
- Sit in the CSE harness `--commit` list. There is no FSRT harness schema yet.
- Fork JSPT. Chart law and `J Sigma J^T` stay in
  [JSPT](https://github.com/giasonpooni/Jacobian-Sensitivity-Propagation-Testbed).
  Pin a SHA when an adapter wraps those objects.

## Where the multi-tool bundle lives

[CSE experiment index](https://github.com/giasonpooni/Construction-State-Estimator-for-BIM/blob/main/docs/experiment-index-v1.md)

```bash
python -m gat.demo.experiment_harness --demo -o out/harness-bundle.json
```

That command is CSE. It does not run FSRT.
