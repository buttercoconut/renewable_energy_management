# Pydantic models for domain entities
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Facility(BaseModel):
    id: int
    name: str
    location: str
    capacity_kw: float
    installed_date: datetime

class EnergyConsumption(BaseModel):
    id: int
    facility_id: int
    timestamp: datetime
    consumption_kwh: float

class SafetyIncident(BaseModel):
    id: int
    facility_id: int
    timestamp: datetime
    description: str
    severity: str
