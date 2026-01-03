def classify_complaint(text):
    text = text.lower()

    categories = {
        "Sanitation": ["garbage", "waste", "trash", "dirty", "dump"],
        "Roads": ["road", "pothole", "street", "bridge"],
        "Electricity": ["electricity", "power", "light", "current", "transformer"],
        "Water": ["water", "pipe", "leak", "supply", "drinking"],
        "Healthcare": ["hospital", "doctor", "ambulance", "medicine"],
        "Public Safety": ["accident", "fire", "crime", "police", "unsafe"]
    }

    for category, keywords in categories.items():
        if any(word in text for word in keywords):
            return category

    return "General"