async def get_safety_report():
    # Placeholder: return static incidents
    return {
        "incidents": [
            {"id": 1, "facility_id": 1, "timestamp": "2024-06-20T10:15:00Z", "description": "Fall from scaffold", "severity": "Minor"},
            {"id": 2, "facility_id": 2, "timestamp": "2024-06-22T14:30:00Z", "description": "Electrical shock", "severity": "Major"},
        ]
    }
