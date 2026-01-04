def assign_priority(text):
    text = text.lower()

    score = 0
    reasons = []

    # SAFETY-CRITICAL (NON-NEGOTIABLE)
    high_keywords = [
        "accident", "fire", "crime", "injured",
        "hospital", "emergency", "ambulance",
        "death", "danger"
    ]

    # IMPORTANT BUT NON-CRITICAL
    medium_keywords = [
        "garbage", "not working", "broken",
        "leak", "overflow", "delay", "days"
    ]

    # Safety check
    if any(word in text for word in high_keywords):
        score += 70
        reasons.append("Public safety risk detected")

    # Civic issue severity
    if any(word in text for word in medium_keywords):
        score += 30
        reasons.append("Essential civic service issue")

    # Final level decision
    if score >= 70:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return level, score, reasons

