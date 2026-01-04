def route_department(category):
    mapping = {
        "Sanitation": "Municipality",
        "Roads": "Public Works Department",
        "Electricity": "Electricity Board",
        "Water": "Water Supply Department",
        "Healthcare": "Health Department",
        "Public Safety": "Police Department",
        "General": "General Administration"
    }
    return mapping.get(category, "General Administration")
