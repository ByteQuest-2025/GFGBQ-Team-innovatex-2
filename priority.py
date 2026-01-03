def assign_priority(text):
    text = text.lower()

    critical_keywords = ["death", "fire", "explosion", "collapse"]
    high_keywords = ["accident", "fire", "danger", "hospital", "child", "crime"]
    medium_keywords = ["delay", "not working", "broken"]

    if any(word in text for word in critical_keywords):
        return "CRITICAL"
    elif any(word in text for word in high_keywords):
        return "HIGH"
    elif any(word in text for word in medium_keywords):
        return "MEDIUM"
    else:
        return "LOW"

