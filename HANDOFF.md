# Handoff — 2026-09-12

> Historical handoff, retained for context. Current development is consolidated on `main`.
> Start with the [contributor brief](docs/COLLABORATOR_BRIEF.md),
> [roadmap](docs/ROADMAP.md) and [repository workflow](AGENTS.md).
>
> Public name is **FSRT** (Fluid State Reconciliation Testbed). Import is `set_lcm`.
> This is measurement reconciliation against a declared balance, not visual
> reconstruction of a fluid volume. License is MIT.

The rest of this file is the 2026-09-12 session state. README.md is the map of
what exists now.

## Known nits (updated)

- Per-seed latency values churn the results JSON on every regeneration.
- Default suite (`pytest -q`, marker `not slow`) takes about 10 minutes.
  Unit gate: `pytest -q -o addopts= -m "not slow and not extended"`.
- License is MIT (`LICENSE`, `pyproject.toml`). The older line that said none
  had been chosen is obsolete.
