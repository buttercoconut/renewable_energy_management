from pydantic import BaseModel
from datetime import datetime

class Facility(BaseModel):
    id: int
    name: str
    location: str
    capacity_kw: float

class EnergyConsumption(BaseModel):
    facility_id: int
    timestamp: datetime
    consumption_kwh: float

class SafetyIncident(BaseModel):
    id: int
    facility_id: int
    timestamp: datetime
    description: str
    severity: str
