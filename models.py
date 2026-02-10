from pydantic import BaseModel
from typing import List


class vehicle_info(BaseModel):
    vehicleId: str
    gpsLatitude: float
    gpsLongitude: float
    gpsAltitude: int
    gpsCourseInDegrees: int
    gpsSignalQuality: int
    gpsFix: bool
    ignitionOn: bool
    crankOn: bool
    speed: int
    odometer: int
    noOfFuelTanks: int

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
