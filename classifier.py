def classify_complaint(text):
    text = text.lower()

    if any(word in text for word in ["garbage", "waste", "trash"]):
        return "Sanitation"
    elif any(word in text for word in ["road", "pothole", "street"]):
        return "Roads"
    elif any(word in text for word in ["electricity", "power", "light"]):
        return "Electricity"
    elif any(word in text for word in ["water", "pipe", "leak"]):
        return "Water"
    elif any(word in text for word in ["hospital", "doctor", "ambulance"]):
        return "Healthcare"
    elif any(word in text for word in ["accident", "fire", "crime", "police"]):
        return "Public Safety"
    else:
        return "General"
