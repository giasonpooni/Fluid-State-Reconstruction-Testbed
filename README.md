# Fluid State Reconciliation Testbed (FSRT)

**Check whether measurements in a fluid network agree with a declared physical balance.**

This is **not** visual reconstruction of a fluid volume. It is not a 3DGS / NeRF / PDE fluid solver. “State reconstruction” here means estimating a physical system from measurements and keeping the evidence needed to challenge that estimate.

| Surface | Name |
|---|---|
| Public name | FSRT (Fluid State Reconciliation Testbed) |
| GitHub repository | `giasonpooni/Fluid-State-Reconstruction-Testbed` |
| Installable project | `fluid-state-reconstruction-testbed` |
| Import | `set_lcm` (historical: state estimate + linear constraint matching) |

FSRT is a Python research toolkit for water levels, flow gauges and storage measurements. It estimates the state of a system, checks the estimate against a declared balance, and keeps a record of the disagreement and any correction.

The aim is to help investigate degrading measurements: **when did the readings stop agreeing, what could explain the difference, and what can this sensor arrangement actually detect?**

## A practical example

A reservoir has measurements of stored water, incoming flow and outgoing flow. Over the same time interval, conservation relates them:

```text
change in stored water = water in − water out
```

If the measurements do not support that balance, FSRT can flag the disagreement and show its size under your stated uncertainties. The cause could be a drifting instrument, an outdated rating curve, an unmeasured inflow, or an unsuitable model. **An alarm starts an investigation; it does not, by itself, identify a broken sensor.**

## Try it

You need [uv](https://docs.astral.sh/uv/getting-started/installation/) and a checkout of this repository. The project supports Python 3.12 and 3.13; its runtime dependency is NumPy.

The checkout is about 50 MB. Most of that is committed NOAA/USGS replay fixtures under `data/` and generated reports under `results/`. The quickstart does not read `data/` and makes no network requests.

```bash
git clone https://github.com/giasonpooni/Fluid-State-Reconstruction-Testbed.git
cd Fluid-State-Reconstruction-Testbed
uv run --frozen --python 3.13 python examples/quickstart.py
```

The example uses two tanks and a declared total of 100 kg. It shows two cases:

- A small disagreement: reconcile the estimate while retaining the original values.
- A large disagreement: flag it and hold the correction so the balance cannot hide the problem.

See the [usage guide](docs/USAGE.md) for the code, expected output, and how to use your own estimates or measurement records.

The results table, readiness notes, and method links that follow are unchanged: every headline number is still pinned by `tests/test_docs_claims.py`.

To run tests:

```bash
# Unit / contract gate (no experiment regeneration)
uv run --frozen --python 3.13 --dev pytest -q -o addopts= -m "not slow and not extended"

# Default suite (excludes only the multi-minute slow marker)
uv run --frozen --python 3.13 --dev pytest -q
```

## License

FSRT is available under the [MIT License](LICENSE).
