# Luminark Logistics Overwatch (LLO) — v1.0

**Predictive Carrier Risk Intelligence for the Modern Brokerage**

**Live Demo:** https://foreverforward760-crypto.github.io/Axiom-yield-broker/

> No metaphysics. No complexity. Just foresight.

---

## What This Is

A self-contained, offline-first carrier vetting and predictive risk platform for freight brokers, 3PLs, and dispatch operations. Built on a proprietary 10-stage operational lifecycle framework by **Meridian Axiom Alignment Technologies (MAAT)**.

**Single `index.html` · No external dependencies · Works offline after first load · All data in localStorage**

---

## Feature Matrix — LLO v1.0

### Core Risk Intelligence
| Feature | Description |
|---------|-------------|
| 0–9 Stage Architecture | Full lifecycle with strength, best-for, advisory, logistics signature per stage |
| Axiom Yield Score (0–100) | Composite from HOS, route volatility, Signal Integrity, recovery debt |
| Stage Momentum Arrows ↑↓→● | Stage velocity per MC tracked in localStorage across sessions |
| Resilience Score (0–100) | Operational elasticity — Green/Yellow/Red with tooltip |
| Carrier Exit Watch ⚠ | Predictive wind-down flag — Stage 7/8/9 + 2-stage drop detected |
| Clarity Audit Toast | Fires when Stage 8 carrier tracked 90+ days |
| Micro-trend (81-stage) | Sub-stage drift stored per MC |
| Container Rule | Cross-MC identity fingerprint — flags phoenix/rebranded carriers |
| System Rigidity Flag | Auto: HOS ≥ 7 + recovery debt ≥ 14 days |
| Integrity Sync Violation | Real-time alert when check-in matches a different MC's company name |

### PDF — Luminark Sentinel Clarity Report
| Feature | Description |
|---------|-------------|
| Two-step Route Lock (S8) | Step 1: Dispatch modal · Step 2: Final gate before PDF export |
| Blocking S8 PDF gate | Stage 8 PDF blocked without Route Lock or Relationship Override |
| Strength box (teal) | Stage-specific carrier strengths — color-exact in print |
| Best-For box (blue) | Ideal load types for current stage — color-exact in print |
| Amber advisory box | Rigidity warning with `.print-fallback` text for B&W printers |
| Route Lock confirmation | Printed in report for legal audit trail |
| Broker Trust Override | Relationship override noted in PDF for legal protection |
| FMCSA data section | Included in report when lookup was performed |
| Legal disclaimer | "This advisory is not a guarantee. Broker responsible for final dispatch decision." |

### FMCSA QCMobile Integration (Optional)
| Feature | Description |
|---------|-------------|
| Toggle on/off | Off by default — never interrupts manual workflow |
| WebKey stored locally | Saved to localStorage only — never transmitted |
| Lookup by MC# | Calls `/carriers/docket-number/{MC}` + `/carriers/{USDOT}/basics` |
| BASIC score mapping | Unsafe Driving + HOS Compliance + Maintenance → Resilience Score |
| Stage auto-suggestion | Authority status + safety rating → suggested stage |
| Graceful fallback | API failure → manual entry, never crashes |

### Lane Pressure Map
| Feature | Description |
|---------|-------------|
| Florida Regional lanes | TPA→ATL, MIA→JAX, TPA→CHI, JAX→HOU, ORL→DFW, MIA→NYC |
| National lanes | ATL→CHI, LAX→DFW, NYC→MIA, CHI→HOU, SEA→PHX, DFW→ATL |
| Filter tabs | All Lanes / 📍 Florida Regional / 🌐 National Lanes |
| Rate multipliers | Stage-based 1.0x–1.25x with 24–48hr advance signal |

### UX & Workflow
| Feature | Description |
|---------|-------------|
| Risk Legend Modal | One-click mid-call dispatch reference (all stages) |
| Signal Check Modal | 5-question live comm vetting → applies to calculator |
| Check-In Exchange | 3-tap carrier portal → live SAP scoring → feed broadcast |
| Operational Velocity Matching | Stabilizer / Volume / Prime / Peak match types |
| Ghost Carrier Filter | MC fraud screening with fractal score |
| Saved Checks | localStorage — survives refresh, last 10 carriers |
| SAP Glossary | 20-row framework → Logistics → Industry translation |

---

## Stage Reference

| Stage | Label | Strength | Best For |
|-------|-------|----------|---------|
| S0 | Ghost / Seed State | — | 3-point vetting only (FMCSA + selfie + 3 refs) |
| S1 | Emergent Startup | Directional intent | Short-haul pilot loads |
| S2 | Standardized Operator | Vessel-stable, strong safety | Hazmat, gov, compliance freight |
| S3 | Reliable Small Fleet | Consistent mid-volume | Regional weekly lanes |
| **S4** | **Established Regional** | **Workhorse · High on-time** | **Contracted freight, dedicated lanes** |
| S5 | Scaling Pivot Point | Max adaptability if managed | Recovery / restoration loads |
| S6 | Optimized Enterprise | Strategic partner | Complex multi-stop, time-sensitive |
| S7 | Recovery Specialist | The Fixer | Crisis loads, emergency recovery |
| S8 | Precision Operator | Flawless record | Fixed-route only + backup required |
| S9 | Market Exit Watch | Transparent, winding down | Verify business continuity only |

---

## Tech Stack
- **Frontend:** HTML5 · CSS3 · Vanilla JavaScript — zero dependencies
- **Persistence:** localStorage — checks, micro-trends, FMCSA keys, stage history
- **FMCSA:** QCMobile API (optional) — WebKey local only
- **Backend (Phase 2):** Flask/Python — `/backend` folder, Render-ready via `render.yaml`

---

**Author:** Richard Leroy Stanfield Jr. — Founder, MAAT  
**Contact:** LuminarkMeridian@gmail.com  
Copyright © 2026 Richard Leroy Stanfield Jr. All rights reserved.
