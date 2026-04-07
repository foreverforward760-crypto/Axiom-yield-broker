# Luminark Logistics Overwatch

**Predictive Intelligence for the Modern Brokerage**

**Live Demo:** https://foreverforward760-crypto.github.io/Axiom-yield-broker/

---

## What This Is

Luminark Logistics Overwatch is a carrier risk scoring platform built on the Stanfield Axiom of Perpetuity (SAP) — a proprietary 10-stage operational risk framework applied to freight logistics. Standard load board tools give you historical compliance data. LLO gives you where the carrier is *going* — by scoring current operating conditions against a predictive failure model.

The platform identifies Stage 8 carriers — those who appear fully compliant but are 24–72 hours from a service failure — before the load is tendered.

---

## Risk Stage Quick Reference

| Stage | Industry Label | Dispatch Action |
|-------|---------------|----------------|
| 0 | Ghost / No Authority | Do not assign. Full vetting required. |
| 1 | New Entrant | Pilot loads only. Monitor first 3. |
| 2 | Scaling Carrier | Standard dry van volume. |
| 3 | Hyper-Growth Risk | Verify asset count. Watch over-booking. |
| **4** | **Tier 1 Reliable** | **Assign highest-value freight.** |
| 5 | Last Off-Ramp | Recovery run only. Last chance before Stage 8. |
| 6 | Peak Window | Assign complex load NOW. 24–72 hr window. |
| 7 | Solo Specialist | Solo long-haul. Full autonomy. Hands-off. |
| **8** | **Eye of the Storm** | **DO NOT DISPATCH. Collapse imminent.** |
| 9 | Dissolution / Exit | Source replacement immediately. |

---

## Core Features

- **Axiom Yield Score (AYS)** — 0–100 predictive risk score. Below 40 = do not dispatch.
- **Stage 8 Detection** — Identifies carriers who look perfect but are 24–72 hrs from failure. The Blind Spot Metric catches what load boards cannot see.
- **Ghost Carrier Filter** — MC number screening. Fraudulent operators show no authentic operational variance — the filter scores that absence as the primary fraud signal.
- **Lane Pressure Map** — Capacity forecasting 24–48 hrs ahead of load board visibility. Stage 8 lanes: 1.15x–1.25x rate multiplier.
- **Risk Legend** — One-click quick reference. Make a dispatch decision in 3 seconds.
- **SAP → Logistics Glossary** — Full translation table from framework language to industry standard terminology.

---

## SAP → Logistics Glossary (Key Terms)

| SAP Term | Industry Translation |
|----------|---------------------|
| Asset Density (P.Stable) | Equipment / Driver Availability |
| Signal Integrity (C.Stable) | Dispatch Responsiveness / Communication Quality |
| Blind Spot Metric (Inversion Principle) | Good Metrics Masking Bad Operations |
| Recovery Debt | Driver Fatigue Accumulation |
| Entropy Load | Failure Probability Trending Up |
| Ghost Score | Fraud Detection Score |
| Lane Pressure Index | Market Tightness Index |

---

## Status

- ✅ Axiom Yield Calculator (client-side)
- ✅ SAP Risk Stage Index — all 10 stages with dispatch guidance
- ✅ Ghost Carrier MC screening
- ✅ Lane Pressure Map with rate multipliers
- ✅ Risk Legend quick-reference modal
- ✅ Full SAP → Logistics glossary and translation table
- ⏳ Backend API integration (Phase 2)
- ⏳ Live carrier data feeds (Phase 2)

**Join Beta Waitlist — Launching April 15, 2026**

---

## Tech Stack

- **Frontend:** Single-file HTML/CSS/JS — GitHub Pages
- **Backend (Phase 2):** Flask/Python REST API — `/backend` folder
- **Deploy config:** `render.yaml`

---

**Author:** Richard Leroy Stanfield Jr.
**Organization:** Meridian Axiom Alignment Technologies (MAAT)
**Contact:** LuminarkMeridian@gmail.com
**Framework:** Stanfield Axiom of Perpetuity (SAP) v3.0

Copyright © 2026 Richard Leroy Stanfield Jr. All rights reserved.
