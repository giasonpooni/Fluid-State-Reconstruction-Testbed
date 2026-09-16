# Map

```mermaid
flowchart LR
  Gauges["gauges / levels"] --> Est["state estimate"]
  Decl["declared balance"] --> Test{"residual vs stated sigma"}
  Est --> Test
  Test -->|small| Rec["reconcile · keep originals"]
  Test -->|large| Flag["flag · do not hide"]
  Test -->|collinear candidates"| Amb["report ambiguity"]
```

Caption: an alarm starts an investigation. It does not name a broken
sensor by itself. Chart changes must leave the physical residual invariant.
JSPT owns A2–A5. This repo does not own V or BIM dispositions.
