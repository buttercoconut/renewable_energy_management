from fastapi import APIRouter
from .models import PowerPlant, EnergyConsumption, SafetyIncident

router = APIRouter(prefix="/api", tags=["api"])

@router.get("/plants", response_model=list[PowerPlant])
async def get_plants():
    return []

@router.get("/consumption", response_model=list[EnergyConsumption])
async def get_consumption():
    return []

@router.get("/incidents", response_model=list[SafetyIncident])
async def get_incidents():
    return []
