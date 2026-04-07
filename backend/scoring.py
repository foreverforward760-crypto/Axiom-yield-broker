# scoring.py — SAP yield logic (server-side only, not exposed to browser)
# Stanfield Axiom of Perpetuity v3.0
# Copyright © 2026 Richard Leroy Stanfield Jr. All rights reserved.

def calculate_yield(hos: int, volatility: int, comm_quality: int, recovery_days: int) -> dict:
    """
    Core SAP Axiom Yield scoring formula.
    Inputs:
        hos            — hours of service remaining (0–11)
        volatility     — route entropy: weather + traffic (0–10)
        comm_quality   — dispatcher communication coherence (0–10)
        recovery_days  — days since last restoration load (0–14)
    Returns:
        { "score": int 0-100, "stage": int 0-9, "tension": int }
    """
    p_stable  = (hos / 11) * 100
    entropy   = (volatility / 10) * 100
    c_stable  = (comm_quality / 10) * 100
    debt      = (recovery_days / 14) * 100

    score = round(
        (p_stable  * 0.30) +
        (c_stable  * 0.25) +
        ((100 - entropy) * 0.25) +
        ((100 - debt)    * 0.20)
    )
    score = max(0, min(100, score))  # clamp to 0–100

    # SAP stage mapping
    if score >= 85:
        stage = 6
    elif score >= 72:
        stage = 4
    elif score >= 58:
        stage = 2
    elif score >= 45:
        stage = 7
    elif score >= 30:
        stage = 5
    elif score >= 15:
        stage = 8
    else:
        stage = 9

    # Inversion tension per stage (from SAP framework)
    tension_map = {0: 0, 1: 28, 2: 42, 3: 55, 4: 22,
                   5: 88, 6: 38, 7: 62, 8: 92, 9: 14}
    tension = tension_map.get(stage, 50)

    # Stage labels for response context
    label_map = {
        0: 'Void / Plenara',  1: 'Navigation',   2: 'Polarity',
        3: 'Expression',      4: 'Foundation',   5: 'Threshold',
        6: 'Integration',     7: 'Analysis',     8: 'Unity / Trap',
        9: 'Release'
    }

    # Dispatch guidance per stage
    guidance_map = {
        4: 'Assign high-value / tight-window loads. Optimal foundation.',
        5: 'Threshold state. Assign restoration load. No hard deadlines.',
        6: 'Peak window — brief. Assign most complex load NOW.',
        7: 'Assign solo, low-communication-demand runs. Monitor closely.',
        8: 'DO NOT assign. False stability. Stage 9 failure imminent.',
        9: 'Exiting state. Seek replacement. Plan contingency.',
        2: 'Building carrier. Reliable for standard volume.',
        3: 'Scaling fast. Watch for over-extension.',
        1: 'New entrant. Pilot load only.',
        0: 'No assignment possible. Ghost or non-entity.',
    }

    return {
        "score":    score,
        "stage":    stage,
        "tension":  tension,
        "label":    label_map.get(stage, 'Unknown'),
        "guidance": guidance_map.get(stage, 'Monitor')
    }
