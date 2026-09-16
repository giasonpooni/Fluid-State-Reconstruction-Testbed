# Handoff — 2026-09-12

> Historical handoff, retained for context. Current development is consolidated on `main`.
> Start with the [contributor brief](docs/COLLABORATOR_BRIEF.md),
> [roadmap](docs/ROADMAP.md) and [repository workflow](AGENTS.md).
>
> Public name: **FSRT** (Fluid State Reconciliation Testbed). Import: `set_lcm`.
> Not visual reconstruction of a fluid volume. License: MIT.

The build moves from the local session that wrote this repository to the cloud
session "FSRT assembly and build". This file is for a session starting cold. README.md
is the map of what exists and what each result does and does not show; this file says
what was in progress, what is decided, and how the work has been done.

## State at handoff

`main` at the time of this note held the Phase 1 slice and its hardening through the
first truth-free real-data report. Later work on `main` superseded several planned
steps below; treat README.md and results/ as current.

## Known nits

- Per-seed latency values churn the results JSON on every regeneration.
- Default suite (`pytest -q`, marker `not slow`) takes about 10 minutes.
  Unit gate: `pytest -q -o addopts= -m "not slow and not extended"`.
- License is MIT (`LICENSE`, `pyproject.toml`). The older line that said none
  had been chosen is obsolete.

Site-selection notes from this handoff remain in
`docs/handoff/usgs_site_selection_2026-09-12.json`.
