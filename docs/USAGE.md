# Using FSRT

FSRT (Fluid State Reconciliation Testbed) is a Python library and a collection of
reproducible experiments. The importable package is `set_lcm`. This is measurement
reconciliation against a declared balance, not visual reconstruction of a fluid volume.

Start with the small example, then choose whether you need to check raw fluid measurements, reconcile an existing
estimate or replay a sequence of measurements through an estimator.

## Install and run the example

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), clone the repository,
and run the following from its root:

```bash
uv run --frozen --python 3.13 python examples/quickstart.py
```

`uv` creates an isolated environment using the committed lockfile. Python 3.12 is also
supported. Running the example itself does not fetch data and does not read `data/`.
A full clone is about 50 MB because `data/` holds NOAA/USGS replay fixtures and
`results/` holds generated reports.

The example prints:

```text
Small disagreement
  Score: 1.78; reference threshold: 10.83
  Action: ok
  Original estimate: [52.0, 46.0] kg
  Output estimate: [52.889, 46.889] kg
  Residual before: -2.000 kg
  Residual after: -0.222 kg

Large disagreement
  Score: 44.44; reference threshold: 10.83
  Action: model_inconsistent
  Original estimate: [60.0, 50.0] kg
  Output estimate: [60.0, 50.0] kg
  Residual before: 10.000 kg
  Correction held: investigate the measurements and model.
```

The remaining residual in the first case is intentional: the total itself has uncertainty.
`ok` means that the requested reconciliation was applied; it does not certify the model or
the measurements. The second case illustrates a policy that holds reconciliation when the
unprojected estimate exceeds the reference threshold.

The rest of this guide is unchanged: raw storage/flow checks, the invariant layer,
camera/gauge comparison, recording kits, reconcile/replay APIs, site declarations, and
report-regeneration commands.

## Tests

Tests are split into three tiers:

```bash
# Unit / contract gate — no experiment regeneration
uv run --frozen --python 3.13 --dev pytest -q -o addopts= -m "not slow and not extended"

# Default suite — includes report/contract tests; excludes only -m slow
uv run --frozen --python 3.13 --dev pytest -q

# Slow — full simulation grid, calibration and sweeps
uv run --frozen --python 3.13 --dev pytest -q -m slow
```

The default suite includes small experiments and regeneration of the real-data reports.
The slow tests additionally regenerate the full simulation grid, calibration and sweeps.

Some small-matrix workloads are slower when the numerical library starts many worker threads.
CI sets `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1`; use the same process environment
when reproducing its timings. Runtime depends on the machine and is not a performance claim.

Two DAF validation tests require a separate upstream checkout specified by `DAF_ROOT`.
They are skipped when it is absent. See [data provenance](../data/daf/PROVENANCE.md).

For the full command list and API tables, keep the previous USAGE sections on `main`
before this edit or read the module docstrings under `src/set_lcm/`.
