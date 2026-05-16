# Maintenance scheduling service (placeholder)
from datetime import datetime, timedelta
from typing import List

class MaintenanceService:
    def __init__(self):
        self.schedule = []  # In-memory schedule list

    def add_maintenance(self, facility_id: int, due_date: datetime, description: str):
        self.schedule.append({"facility_id": facility_id, "due_date": due_date, "description": description})

    def get_upcoming(self, days: int = 30) -> List[dict]:
        cutoff = datetime.utcnow() + timedelta(days=days)
        return [s for s in self.schedule if s["due_date"] <= cutoff]
