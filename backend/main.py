from fastapi import FastAPI , status , Depends , HTTPException
from pydantic import BaseModel , Field
import models
from typing import List, Annotated
from database import engine , sessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime, date as Date, time as Time
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
    speed: int = Field(..., ge=0)
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
    currentGear: int
    fuelLevelPercent: float

    batterySOC: List[float]
    noOfBatteryPacks: int

    imei: str
    registrationNumber: str
    eventDateTime: datetime


class StaticDataResponse(BaseModel):
    id: int
    vehicleId: str
    imei: str
    registrationNumber: str
    noOfFuelTanks: int
    primaryFuelTankCapacity: int
    secondaryFuelTankCapacity: int
    noOfBatteryPacks: int


class DynamicDataResponse(BaseModel):
    id: int
    vehicleId: str
    latitude: float
    longitude: float
    altitude: int
    speed: int
    satellites: int
    ignition: bool
    gpsFix: bool
    gsmSignal: int
    odometer: int
    fuelLevel: int
    batteryVoltage: float
    accelX: float
    accelY: float
    accelZ: float
    status: str
    gear: int
    fuelLevelPercent: float
    batterySOC: List[float]
    timestamp: str


class VehicleTelemetryResponse(BaseModel):
    vehicle: str
    date: str
    time: str
    staticData: StaticDataResponse
    dynamicData: DynamicDataResponse


def getdb():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session , Depends(getdb)]


@app.post("/gps/new-location", status_code=status.HTTP_201_CREATED)
async def vehicle_infor(post_info: vehicle_info , db: db_dependency):

    vehicle = db.query(models.vehicle_info).filter(
        models.vehicle_info.vehicleId == post_info.vehicleId
    ).first()

    if not vehicle:
        vehicle = models.vehicle_info(
            vehicleId = post_info.vehicleId,
            imei = post_info.imei,
            registrationNumber = post_info.registrationNumber,
            no_Of_Fuel_Tanks = post_info.no_Of_Fuel_Tanks,
            primaryFuelTankCapacity = post_info.primaryFuelTankCapacity,
            secondaryFuelTankCapacity1 = post_info.secondaryFuelTankCapacity1,
            noOfBatteryPacks = post_info.noOfBatteryPacks
        )

        try:
            db.add(vehicle)
            db.commit()
            db.refresh(vehicle)
        except IntegrityError:
            db.rollback()
            raise HTTPException(409 , "Vehicle already exists")

    
    telemetry = models.Vehicle_telemetry(
        vehicleId = post_info.vehicleId,

        gps_Latitude = post_info.gps_Latitude,
        gps_Longitude = post_info.gps_Longitude,
        gps_Altitude = post_info.gps_Altitude,
        gps_CourseInDegrees = post_info.gps_CourseInDegrees,
        gps_SignalQuality = post_info.gps_SignalQuality,
        gps_Fix = post_info.gps_Fix,

        ignitionOn = post_info.ignitionOn,
        crankOn = post_info.crankOn,
        speed = post_info.speed,
        odometer = post_info.odometer,

        PrimaryFuelLevel = post_info.PrimaryFuelLevel,
        SecondaryFuelLevel1 = post_info.SecondaryFuelLevel1,
        defLevel = post_info.defLevel,

        backupBatteryVoltage = post_info.backupBatteryVoltage,
        vehicleBatteryVoltage = post_info.vehicleBatteryVoltage,

        accelX = post_info.accelX,
        accelY = post_info.accelY,
        accelZ = post_info.accelZ,

        gyroX = post_info.gyroX,
        gyroY = post_info.gyroY,
        gyroZ = post_info.gyroZ,

        acStatus = post_info.acStatus,
        vehicleStatus = post_info.vehicleStatus,
        engineRunHour = post_info.engineRunHour,
        currentGear = post_info.currentGear,
        fuelLevelPercent = post_info.fuelLevelPercent,

        batterySOC = post_info.batterySOC,
        eventDateTime = post_info.eventDateTime
    )

    db.add(telemetry)
    db.commit()
    db.refresh(telemetry)

    return {"message": "Telemetry stored successfully"}


@app.get("/gps/vehicle/{vehicle_id}/telemetry", response_model=VehicleTelemetryResponse)
async def get_vehicle_telemetry(vehicle_id: str, date: Date, time: Time, db: db_dependency):
    target_dt = datetime.combine(date, time)

    vehicle = db.query(models.vehicle_info).filter(
        models.vehicle_info.vehicleId == vehicle_id
    ).first()

    if not vehicle:
        raise HTTPException(404, "Vehicle not found")

    telemetry = db.query(models.Vehicle_telemetry).filter(
        models.Vehicle_telemetry.vehicleId == vehicle_id,
        models.Vehicle_telemetry.eventDateTime == target_dt
    ).first()

    if not telemetry:
        raise HTTPException(404, "No telemetry found for the given vehicle, date, and time")

    return VehicleTelemetryResponse(
        vehicle=vehicle_id,
        date=str(date),
        time=str(time),
        staticData=StaticDataResponse(
            id=vehicle.id,
            vehicleId=vehicle.vehicleId,
            imei=vehicle.imei,
            registrationNumber=vehicle.registrationNumber,
            noOfFuelTanks=vehicle.no_Of_Fuel_Tanks,
            primaryFuelTankCapacity=vehicle.primaryFuelTankCapacity,
            secondaryFuelTankCapacity=vehicle.secondaryFuelTankCapacity1,
            noOfBatteryPacks=vehicle.noOfBatteryPacks
        ),
        dynamicData=DynamicDataResponse(
            id=telemetry.id,
            vehicleId=telemetry.vehicleId,
            latitude=telemetry.gps_Latitude,
            longitude=telemetry.gps_Longitude,
            altitude=telemetry.gps_Altitude,
            speed=telemetry.speed,
            satellites=telemetry.gps_SignalQuality,
            ignition=telemetry.ignitionOn,
            gpsFix=telemetry.gps_Fix,
            gsmSignal=telemetry.gps_SignalQuality,
            odometer=telemetry.odometer,
            fuelLevel=telemetry.PrimaryFuelLevel,
            batteryVoltage=telemetry.vehicleBatteryVoltage,
            accelX=telemetry.accelX,
            accelY=telemetry.accelY,
            accelZ=telemetry.accelZ,
            status=telemetry.vehicleStatus,
            gear=telemetry.currentGear,
            fuelLevelPercent=telemetry.fuelLevelPercent,
            batterySOC=telemetry.batterySOC,
            timestamp=str(time)
        )
    )

@app.get("/vehicles")
def get_all_vehicles(db: db_dependency):
    vehicles = db.query(models.vehicle_info.vehicleId).distinct().all()
    return [v.vehicleId for v in vehicles]



@app.get("/times/vehicle/{vehicle_id}/{date}")
def get_available_times(vehicle_id: str, date: Date, db: db_dependency):
    times = (
        db.query(models.Vehicle_telemetry.eventDateTime)
        .filter(
            models.Vehicle_telemetry.vehicleId == vehicle_id,
            models.Vehicle_telemetry.eventDateTime >= datetime.combine(date, Time.min),
            models.Vehicle_telemetry.eventDateTime <= datetime.combine(date, Time.max),
        )
        .distinct()
        .all()
    )
    return [t.eventDateTime.strftime("%H:%M:%S") for t in times]