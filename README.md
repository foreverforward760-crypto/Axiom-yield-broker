# Axiom Yield Broker — Carrier Risk Intelligence Platform

**Live Demo:** https://foreverforward760-crypto.github.io/Axiom-yield-broker/

## What This Is

Axiom Yield Broker is a predictive carrier risk scoring platform for freight brokers, 3PLs, and dispatch operations. It identifies high-risk carriers before load tender — not after the service failure.

Standard load board tools show you historical compliance data. AYB shows you where a carrier is *going* by scoring four current operating conditions against the SAP Risk Stage Index.

## Core Features

- **Axiom Yield Score (AYS)** — 0–100 composite risk score from HOS, route volatility, Signal Integrity, and recovery debt. Maps to SAP risk stage. Any score below 40 is a do-not-dispatch signal.
- **Stage 8 Detection (Eye of the Storm)** — Identifies carriers who appear fully compliant but are 24–72 hours from a service failure. The Blind Spot Metric catches what load boards cannot see.
- **Ghost Carrier Filter** — MC number screening against synthetic carrier patterns. Fraudulent operators show no authentic operational variance — the filter scores that absence as the primary fraud signal.
- **Lane Pressure Map** — Corridor-level capacity forecasting staged 24–48 hours ahead of load board visibility with rate multiplier guidance.

## Risk Stage Quick Reference

| Stage | Label | Dispatch Action |
|-------|-------|----------------|
| 0 | Ghost / No Authority | Do not use |
| 1 | New Entrant | Pilot loads only |
| 2 | Established / Building | Standard volume lanes |
| 3 | Scaling / Volatile Growth | Monitor over-extension |
| 4 | **Prime Carrier** | **Assign highest-value loads** |
| 5 | Threshold / Point of No Return | Recovery run — last off-ramp |
| 6 | Peak Performance Window | Assign complex load NOW |
| 7 | Solo Operator / Peak Isolation | Autonomy — solo long-haul |
| 8 | **Eye of the Storm** | **DO NOT DISPATCH** |
| 9 | Exit / Dissolution | Source replacement immediately |

## Status

- ✅ Carrier risk calculator (client-side)
- ✅ SAP Risk Stage Index with dispatch guidance
- ✅ Ghost carrier MC screening
- ✅ Lane pressure map with rate multipliers
- ✅ Industry glossary
- ⏳ Backend API integration (Phase 2)
- ⏳ Live carrier data feeds (Phase 2)

**Join Beta Waitlist — Launching April 15, 2026**

## Tech Stack

- **Frontend:** Single-file HTML/CSS/JS — deployable via GitHub Pages
- **Backend (Phase 2):** Flask/Python REST API — see `/backend` folder
- **Deploy:** Render.com via `render.yaml`

## Framework

Built on **Stanfield's Axiom of Perpetuity (SAP) v3.0**

**Author:** Richard Leroy Stanfield Jr.
**Organization:** Meridian Axiom Alignment Technologies (MAAT)
**Contact:** LuminarkMeridian@gmail.com

---

Copyright © 2026 Richard Leroy Stanfield Jr. All rights reserved.
