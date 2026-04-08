# Luminark Logistics Overwatch

**Predictive Intelligence for the Modern Brokerage**

**Live Demo:** https://foreverforward760-crypto.github.io/Axiom-yield-broker/

---

## What This Is

Predictive carrier risk platform for freight brokers, 3PLs, and dispatch operations. Identifies Stage 8 carriers — those who appear fully compliant but are 24–72 hours from a service failure — before the load is tendered.

Built on **Stanfield's Axiom of Perpetuity (SAP) v3.0** by Meridian Axiom Alignment Technologies (MAAT).

---

## Features (Current Intel Feed)

| Feature | Status | Description |
|---------|--------|-------------|
| Axiom Yield Score | ✅ Live | 0–100 predictive reliability score from 4 dispatch metrics |
| Stage 8 Detection | ✅ Live | Eye-of-Storm identification 24–72 hrs before service failure |
| System Rigidity Flag | ✅ Live | Auto-fires: HOS ≥ 7 + recovery debt ≥ 14 days |
| **Check-In Exchange** | ✅ Live | **Dynamic Capacity Exchange — carrier self-reporting with live SAP scoring** |
| **Operational Velocity Matching** | ✅ Live | **Stabilizer / Volume / Red Flag Block — 3 broker match types** |
| **3-Tap Carrier Portal** | ✅ Live | **Carrier check-in form → live Yield Score → feed broadcast** |
| Signal Check Modal | ✅ Live | 5-question comm vetting — applies to calculator |
| Risk Legend Modal | ✅ Live | One-click mid-call dispatch reference |
| Ghost Carrier Filter | ✅ Live | MC fraud pattern screening |
| Lane Pressure Map | ✅ Live | Corridor capacity forecasting + rate multipliers |
| PDF Risk Report | ✅ Live | Download carrier risk report for TMS attachment |
| Saved Checks | ✅ Live | localStorage — survives refresh, last 10 carriers |
| SAP Glossary | ✅ Live | 20-row SAP → Logistics → Industry translation table |
| Backend API | ⏳ Phase 2 | Flask/Python — `/backend` folder |
| Live GPS Integration | ⏳ Phase 2 | Real carrier location verification |
| TMS Integration | ⏳ Phase 2 | CRM + load board API hooks |

---

## Check-In Exchange — How It Works

The Check-In Exchange transforms LLO from a **Static Vetting Tool** into a **Dynamic Capacity Exchange**.

### For Carriers (3-Tap Check-In)
1. **Tap 1** — Confirm location (city/state, GPS-verifiable on mobile)
2. **Tap 2** — Select availability window (Now / 1hr / 2–4hrs / Tomorrow AM)
3. **Tap 3** — Select intended destination / heading city

Carrier submits → Axiom Yield Score calculated live → broadcast to active brokers

### Operational Velocity Matching Engine

| Match Type | Trigger | Carrier Surfaced |
|-----------|---------|-----------------|
| 🔷 Stabilizer Match | Broker has late/abandoned load | Stage 7 — Isolated Specialist |
| 📈 Volume Match | Broker has 5+ loads one lane | Stage 2/3 — Scaling Carrier |
| 🟢 Prime Match | Standard high-value tender | Stage 4 — Tier 1 Reliable |
| ⚡ Peak Window | Time-critical complex load | Stage 6 — Hot Hand |
| 🚫 Red Flag Block | Stage 8 checks in | Silently deprioritized — shown last |

### Revenue Model
- Brokers pay for Overwatch (risk assessment subscription)
- Carriers pay priority check-in fee OR use free to prove Signal Integrity and earn better loads

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

**Author:** Richard Leroy Stanfield Jr. — Founder, MAAT  
**Contact:** LuminarkMeridian@gmail.com  
Copyright © 2026 Richard Leroy Stanfield Jr. All rights reserved.
