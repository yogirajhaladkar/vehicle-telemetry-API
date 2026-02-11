from sqlalchemy import Column, Integer, String, Float, Boolean, JSON
from database import Base
from sqlalchemy.orm import Mapped, mapped_column




class VehicleInfo(Base):
    __tablename__ = "vehicle_telemetry"

    id = Column(Integer, primary_key=True, index=True)

    vehicleId = Column(String(64))
    gps_Latitude : Mapped[float] = mapped_column(Float)
    gps_Longitude : Mapped[float] = mapped_column(Float)
    gps_Altitude = Column(Integer)
    gps_CourseInDegrees = Column(Integer)
    gps_SignalQuality = Column(Integer)
    gps_Fix = Column(Boolean)

    ignitionOn = Column(Boolean)
    crankOn = Column(Boolean)
    speed = Column(Integer)
    odometer = Column(Integer)
    no_Of_Fuel_Tanks = Column(Integer)

    PrimaryFuelLevel = Column(Integer)
    primaryFuelTankCapacity = Column(Integer)
    SecondaryFuelLevel1 = Column(Integer)
    secondaryFuelTankCapacity1 = Column(Integer)
    defLevel = Column(Integer)

    backupBatteryVoltage : Mapped[float] = mapped_column(Float)
    vehicleBatteryVoltage : Mapped[float] = mapped_column(Float)

    accelX : Mapped[float] = mapped_column(Float)
    accelY : Mapped[float] = mapped_column(Float)
    accelZ : Mapped[float] = mapped_column(Float)
    gyroX : Mapped[float] = mapped_column(Float)
    gyroY : Mapped[float] = mapped_column(Float)
    gyroZ : Mapped[float] = mapped_column(Float)

    acStatus = Column(Boolean)
    vehicleStatus = Column(String(64))
    engineRunHour : Mapped[float] = mapped_column(Float)
    currentGear : Mapped[float] = mapped_column(Float)
    fuelLevelPercent : Mapped[float] = mapped_column(Float)

    batterySOC = Column(JSON)
    noOfBatteryPacks = Column(Integer)

    imei = Column(String(32))
    registrationNumber = Column(String(32))
    eventDateTime = Column(String(64))

