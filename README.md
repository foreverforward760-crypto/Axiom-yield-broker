# Luminark Logistics Overwatch

**Predictive Intelligence for the Modern Brokerage**

**Live Demo:** https://foreverforward760-crypto.github.io/Axiom-yield-broker/

---

## What This Is

Predictive carrier risk platform for freight brokers, 3PLs, and dispatch operations. Identifies Stage 8 carriers — those who appear fully compliant but are 24–72 hours from a service failure — before the load is tendered.

Built on **Stanfield's Axiom of Perpetuity (SAP) v3.0** — proprietary framework by Meridian Axiom Alignment Technologies (MAAT).

---

## Features (Current Intel Feed)

| Feature | Status | Description |
|---------|--------|-------------|
| Axiom Yield Score | ✅ Live | 0–100 predictive reliability score from 4 dispatch metrics |
| Stage 8 Detection | ✅ Live | Eye-of-Storm identification 24–72 hrs before failure |
| System Rigidity Flag | ✅ Live | Auto-fires when HOS ≥ 7 + recovery debt ≥ 14 days |
| Signal Check Modal | ✅ Live | 5-question comm vetting tool — applies score to calculator |
| Risk Legend Modal | ✅ Live | One-click mid-call dispatch reference |
| Ghost Carrier Filter | ✅ Live | MC fraud pattern screening |
| Lane Pressure Map | ✅ Live | Corridor capacity forecasting + rate multipliers |
| PDF Risk Report | ✅ Live | Download carrier risk report for TMS attachment |
| Saved Checks | ✅ Live | localStorage — survives page refresh, last 10 carriers |
| Input Validation | ✅ Live | All inputs clamped, edge cases handled |
| Mobile Responsive | ✅ Live | Touch-optimized, finger-friendly targets |
| SAP Glossary | ✅ Live | 20-row SAP → Logistics → Industry translation table |
| Backend API | ⏳ Phase 2 | Flask/Python — see `/backend` folder |
| Live Carrier Feeds | ⏳ Phase 2 | DAT / TruckerTools integration |

---

## Risk Stage Quick Reference

| Stage | Industry Term | Action |
|-------|--------------|--------|
| S0 | Ghost / No MC History | Full vetting required |
| S1 | New Entrant / Unproven | Pilot loads only |
| S2 | Scaling Carrier | Standard volume lanes |
| S3 | Hyper-Growth Risk | Verify assets before dispatch |
| **S4** | **Tier 1 Reliable** | **Assign highest-value loads** |
| S5 | Last Chance Recovery | Recovery miles — last off-ramp |
| S6 | Hot Hand / Peak Window | Assign complex load NOW |
| S7 | Isolated Specialist | Solo long-haul, full autonomy |
| **S8** | **Eye of the Storm** | **DO NOT DISPATCH** |
| S9 | Exit / Dissolution | Source replacement immediately |

---

## Tech Stack

- **Frontend:** Single-file HTML/CSS/JS — GitHub Pages deployable, zero dependencies
- **Backend (Phase 2):** Flask/Python REST API — `/backend` folder, Render-ready via `render.yaml`

---

**Author:** Richard Leroy Stanfield Jr. — Founder, MAAT  
**Contact:** LuminarkMeridian@gmail.com  
Copyright © 2026 Richard Leroy Stanfield Jr. All rights reserved.
