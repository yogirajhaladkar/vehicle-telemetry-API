from fastapi import FastAPI  , status , Depends , HTTPException
from pydantic import BaseModel , Field
import models
from typing import List,Annotated
from database import engine ,sessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
app = FastAPI()

models.Base.metadata.create_all(bind=engine)


class vehicle_info(BaseModel):

    vehicleId: str
    gps_Latitude: float
    gps_Longitude: float
    gps_Altitude: int
    gps_CourseInDegrees: int
    gps_SignalQuality: int
    gps_Fix: bool
    ignitionOn: bool
    crankOn: bool
    speed: int= Field(..., ge=0)
    odometer: int
    no_Of_Fuel_Tanks: int

    PrimaryFuelLevel: int
    primaryFuelTankCapacity: int
    SecondaryFuelLevel1: int
    secondaryFuelTankCapacity1: int
    defLevel: int

    backupBatteryVoltage: float
    vehicleBatteryVoltage: float

    accelX: float
    accelY: float
    accelZ: float
    gyroX: float
    gyroY: float
    gyroZ: float

    acStatus: bool
    vehicleStatus: str
    engineRunHour: float
    currentGear: float
    fuelLevelPercent: float

    batterySOC: List[float]
    noOfBatteryPacks: int

    imei: str
    registrationNumber: str
    eventDateTime: str

def getdb():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session , Depends(getdb)]


@app.post("/gps/new-location",status_code=status.HTTP_201_CREATED)
async def vehicle_infor(post_info : vehicle_info , db : db_dependency):
    db_info = models.VehicleInfo(**post_info.model_dump())
    try:
        db.add(db_info)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(409 , "vehicle already exist")

    return {"message": "Data inserted to vehicle telemetry successfully!!"}



