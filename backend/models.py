from sqlalchemy import Integer, String, Float, Boolean, JSON, DateTime
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class vehicle_info(Base):
    __tablename__ = "vehicle_info"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    vehicleId: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    imei: Mapped[str] = mapped_column(String(32))
    registrationNumber: Mapped[str] = mapped_column(String(32))
    no_Of_Fuel_Tanks: Mapped[int] = mapped_column(Integer)
    primaryFuelTankCapacity: Mapped[int] = mapped_column(Integer)
    secondaryFuelTankCapacity1: Mapped[int] = mapped_column(Integer)
    noOfBatteryPacks: Mapped[int] = mapped_column(Integer)

    


class Vehicle_telemetry(Base):
    __tablename__ = "vehicle_telemetry"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    vehicleId: Mapped[str] = mapped_column(String(64), index=True)

    gps_Latitude: Mapped[float] = mapped_column(Float)
    gps_Longitude: Mapped[float] = mapped_column(Float)
    gps_Altitude: Mapped[int] = mapped_column(Integer)
    gps_CourseInDegrees: Mapped[int] = mapped_column(Integer)
    gps_SignalQuality: Mapped[int] = mapped_column(Integer)
    gps_Fix: Mapped[bool] = mapped_column(Boolean)

    ignitionOn: Mapped[bool] = mapped_column(Boolean)
    crankOn: Mapped[bool] = mapped_column(Boolean)
    speed: Mapped[int] = mapped_column(Integer)
    odometer: Mapped[int] = mapped_column(Integer)
    PrimaryFuelLevel: Mapped[int] = mapped_column(Integer)
    SecondaryFuelLevel1: Mapped[int] = mapped_column(Integer)
    defLevel: Mapped[int] = mapped_column(Integer)
    backupBatteryVoltage: Mapped[float] = mapped_column(Float)
    vehicleBatteryVoltage: Mapped[float] = mapped_column(Float)

    accelX: Mapped[float] = mapped_column(Float)
    accelY: Mapped[float] = mapped_column(Float)
    accelZ: Mapped[float] = mapped_column(Float)
    gyroX: Mapped[float] = mapped_column(Float)
    gyroY: Mapped[float] = mapped_column(Float)
    gyroZ: Mapped[float] = mapped_column(Float)

    acStatus: Mapped[bool] = mapped_column(Boolean)
    vehicleStatus: Mapped[str] = mapped_column(String(64))
    engineRunHour: Mapped[float] = mapped_column(Float)
    currentGear: Mapped[int] = mapped_column(Integer)
    fuelLevelPercent: Mapped[float] = mapped_column(Float)
    batterySOC: Mapped[list[float]] = mapped_column(JSON)

    eventDateTime: Mapped[DateTime] = mapped_column(DateTime, index=True)

    
