from fastapi import APIRouter
from ..services.energy_prediction_service import predict_energy
from ..services.maintenance_service import get_maintenance_schedule
from ..services.safety_service import get_safety_report

router = APIRouter(prefix="/api", tags=["energy"])

@router.get("/predict")
async def predict():
    return await predict_energy()

@router.get("/maintenance")
async def maintenance():
    return await get_maintenance_schedule()

@router.get("/safety")
async def safety():
    return await get_safety_report()
