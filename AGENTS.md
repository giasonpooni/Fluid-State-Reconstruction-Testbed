# Development workflow

Maintain FSRT as one project on `main`.

- Work directly on `main` and push completed, validated changes to `origin/main`.
- Do not create development branches, separate project copies, or pull requests unless
  the user explicitly requests them.
- Fetch before pushing, preserve concurrent work, and never force-push `main`.
- Remove obsolete branches only after reviewing their unique work and incorporating
  the accepted changes into `main`.
- Run checks appropriate to the change. Preserve source provenance in generated reports;
  update reports through their generators when their results change.
- Keep the README focused on delivered functionality. Mark research extensions as planned
  until implemented and validated. Development remains focused on fluid systems.
- A2-A5 are owned by JSPT. Pin a SHA (see docs/JSPT_PIN.md). Do not copy JSPT
  coordinates into this tree. Do not put tank ids or declaration text into JSPT.
