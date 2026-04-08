# Luminark Logistics Overwatch (LLO)

**Predictive Intelligence for the Modern Brokerage · SAP v3.0**

**Live Demo:** https://foreverforward760-crypto.github.io/Axiom-yield-broker/

> No metaphysics. No complexity. Just foresight.

---

## What This Is

A self-contained, offline-first carrier vetting and risk intelligence platform for freight brokers, 3PLs, and dispatch operations. Built on **Stanfield's Axiom of Perpetuity (SAP)** by Meridian Axiom Alignment Technologies (MAAT).

Single `index.html` file · No external dependencies · Works offline after first load · All data in localStorage

---

## Full Feature Matrix

### Core Intelligence
| Feature | Description |
|---------|-------------|
| **0–9 Stage Architecture** | Full SAP lifecycle with strength, best-for, advisory, logistics signature per stage |
| **Axiom Yield Score (0–100)** | Composite from HOS, route volatility, Signal Integrity, recovery debt |
| **Stage Momentum Arrows ↑↓→●** | Stage velocity per MC tracked in localStorage |
| **Resilience Score (0–100)** | Operational elasticity — turnover, HOS violations, detention, comms |
| **Carrier Exit Watch ⚠** | Predictive dissolution flag — Stage 7/8/9 + 2-stage drop |
| **Clarity Audit Toast** | Fires when S8 carrier tracked for 90+ days |
| **Micro-trend (81-stage)** | Sub-stage drift stored per MC |
| **Container Rule** | Cross-MC identity fingerprint for phoenix carrier detection |
| **System Rigidity Flag** | Auto: HOS ≥ 7 + recovery debt ≥ 14 days |

### PDF — Luminark Sentinel Clarity Report
| Feature | Description |
|---------|-------------|
| **Two-step Route Lock (S8)** | Step 1: Route Lock modal before dispatch · Step 2: Final confirmation before PDF export |
| **Blocking S8 PDF gate** | Stage 8 PDF blocked without Route Lock or Relationship Override |
| **Strength box** | Teal — stage-specific carrier strengths (print-color-exact) |
| **Best-For box** | Blue — ideal load types for this stage |
| **Dispatch advisory** | Full logistics guidance + stage advisory |
| **Rigidity warning** | Amber advisory box for S8 and rigidity-flagged carriers |
| **Route Lock confirmation** | Prints locked confirmation text in the report |
| **Broker Trust Override** | Relationship override noted in PDF for legal protection |
| **FMCSA data section** | Included if FMCSA lookup was performed |
| **Resilience Score** | Printed with color coding |

### FMCSA QCMobile Integration (Optional)
| Feature | Description |
|---------|-------------|
| **Toggle on/off** | Defaults off — never interferes with manual workflow |
| **WebKey stored locally** | Saved to localStorage only · Never transmitted to Luminark |
| **Lookup by MC#** | Calls `/carriers/docket-number/{MC}` endpoint |
| **BASIC scores** | Calls `/carriers/{USDOT}/basics` for Unsafe Driving, HOS, Maintenance |
| **Auto-map to Resilience** | FMCSA BASIC scores → Resilience Score calculation |
| **Stage suggestion** | Auto-suggests stage from authority status + safety rating |
| **Graceful fallback** | API failure → manual entry, never crashes the app |
| **FMCSA data in PDF** | Included in Sentinel Clarity Report when lookup was performed |
| **Get WebKey** | mobile.fmcsa.dot.gov → Sign in with Login.gov → My WebKeys |

### UX & Workflow
| Feature | Description |
|---------|-------------|
| **Risk Legend Modal** | One-click mid-call dispatch reference (all stages) |
| **Signal Check Modal** | 5-question comm vetting → applies score to calculator |
| **Check-In Exchange** | 3-tap carrier portal → live SAP scoring → feed broadcast |
| **Operational Velocity Matching** | Stabilizer / Volume / Prime / Peak / Red Flag |
| **Ghost Carrier Filter** | MC fraud pattern screening with fractal score |
| **Lane Pressure Map** | Corridor capacity forecasting + rate multipliers |
| **Saved Checks** | localStorage — survives refresh, last 10 carriers |
| **SAP Glossary** | 20-row SAP → Logistics → Industry translation |
| **Advisory over Enforcement** | Every stage framed with strengths, broker autonomy preserved |

---

## Stage Reference

| Stage | Label | Strength | Best For | Advisory |
|-------|-------|----------|---------|---------|
| S0 | Ghost / Seed State | None | 3-point vetting only | Identity risk — FMCSA + selfie + 3 refs |
| S1 | Emergent Startup | Directional intent | Short-haul pilot loads | Rapid tumble risk |
| S2 | Standardized Operator | Vessel-stable, strong safety | Hazmat, gov, compliance freight | Long-term contract candidate |
| S3 | Reliable Small Fleet | Consistent mid-volume | Regional weekly lanes | Monitor driver retention |
| **S4** | **Established Regional** | **Workhorse · High on-time** | **Contracted freight, dedicated lanes** | **Core carrier program — healthiest stage** |
| S5 | Scaling Pivot Point | Max adaptability if managed | Recovery / restoration loads | Critical decision point |
| S6 | Optimized Enterprise | Strategic partner | Complex multi-stop, time-sensitive | Watch for brittle over-optimization |
| S7 | Recovery Specialist | The Fixer | Crisis loads, emergency recovery | High risk/reward — verify insurance |
| S8 | Precision Operator | Flawless record, systemic consistency | Fixed-route only | ⚠ Zero deviation tolerance |
| S9 | Market Exit Watch | Experience, winding down | Trust only with 14-day confirmation | Predictive dissolution risk |

---

## Technical Architecture
- **Frontend:** HTML5 · CSS3 · Vanilla JavaScript (zero dependencies)
- **Persistence:** localStorage only — checks, micro-trends, container fingerprints, FMCSA keys
- **FMCSA:** QCMobile API (optional) — WebKey stored locally, never transmitted
- **Offline:** Works fully offline after first load
- **Backend Phase 2:** Flask/Python REST API — `/backend` folder, Render-ready via `render.yaml`

---

**Author:** Richard Leroy Stanfield Jr. — Founder, MAAT  
**Contact:** LuminarkMeridian@gmail.com  
Copyright © 2026 Richard Leroy Stanfield Jr. All rights reserved.
