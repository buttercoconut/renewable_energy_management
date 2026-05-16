# Safety incident tracking service (placeholder)
from datetime import datetime
from typing import List

class SafetyService:
    def __init__(self):
        self.incidents = []  # In-memory incidents list

    def report_incident(self, facility_id: int, description: str, severity: str):
        self.incidents.append({"facility_id": facility_id, "timestamp": datetime.utcnow(), "description": description, "severity": severity})

    def get_incidents(self, facility_id: int) -> List[dict]:
        return [i for i in self.incidents if i["facility_id"] == facility_id]
