# Luminark Logistics Overwatch — Carrier Scoring Prototype

**Status: prototype. Predictive accuracy has not been established.**

This repository contains a browser-based carrier scoring interface and a small Python backend. It explores applying a 0–9 operational lifecycle framework to selected carrier and route inputs.

## What is present

- A single-page browser interface.
- Local browser storage for selected carrier records and user-entered data.
- A Python scoring function that combines hours-of-service remaining, route volatility, communication quality, and recovery days into a deterministic score.
- A fixed set of score bands, stage labels, and advisory text.
- Deployment configuration for a possible hosted demonstration.

## Important limitations

The current backend formula is a hand-defined weighted score and threshold map. It is not a trained predictive model. The repository does not establish that it predicts carrier failure, fraud, accidents, late delivery, or future market conditions.

A score or stage generated from user-entered or default values is not a verified carrier risk assessment. The tool has not been shown to outperform existing methods, and no prospective accuracy, false-positive rate, false-negative rate, or customer outcome has been established.

The application should be treated as an exploratory decision-support prototype. It must not be used as the sole basis for dispatch, safety, insurance, lending, or other consequential decisions.

## Conceptual provenance

The project owner states that the underlying concepts, product idea, and 0-9-0 / SAP framework applications in this repository originated with him. AI systems generated the implementation code and suggested technical mechanisms used to express those concepts. NSDT and the Container Rule were introduced by AI as supporting implementation mechanisms within the owner's framework, not as independent conceptual origins.

This records the project owner's account; it is not a legal determination of copyright ownership, inventorship, or exclusive rights.

## Validation required

A credible pilot would require authorized carrier and ELD data, a defined prediction target and time window, time-separated test data, comparison with existing baselines, and prospective measurement of outcomes.

## Rights and provenance

The repository owner has disclosed AI-assisted development. Authorship, third-party components, dependencies, and licensing require review before commercial distribution. No patent application or patent protection is represented here.
