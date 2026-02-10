from fastapi import FastAPI  , status , Body
from models import vehicle_info
from typing import Dict , Any 
from database import connect
import json

app = FastAPI()

@app.post("/post_vehivcle_update")
def vehicle_infor(df : vehicle_info):
    conn = connect()
    cursor = conn.cursor()

    query = """ 
    INSERT INTO vehicle_telemetry (

    vehicle_id, imei, registration_number,
        gps_latitude, gps_longitude, gps_altitude,
        gps_course_in_degrees, gps_signal_quality, gps_fix,
        ignition_on, crank_on, speed, odometer,
        vehicle_status, ac_status,
        no_of_fuel_tanks,
        primary_fuel_level, primary_fuel_tank_capacity,
        secondary_fuel_level1, secondary_fuel_tank_capacity1,
        def_level, fuel_level_percent,
        backup_battery_voltage, vehicle_battery_voltage,
        no_of_battery_packs,
        battery_soc,
        accel_x, accel_y, accel_z,
        gyro_x, gyro_y, gyro_z,
        engine_run_hour, current_gear,
        event_date_time
    
    )
    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)
    """
    values = (
        df.vehicleId,
        df.imei,
        df.registrationNumber,

        df.gpsLatitude,
        df.gpsLongitude,
        df.gpsAltitude,
        df.gpsCourseInDegrees,
        df.gpsSignalQuality,
        df.gpsFix,

        df.ignitionOn,
        df.crankOn,
        df.speed,
        df.odometer,

        df.vehicleStatus,
        df.acStatus,

        df.noOfFuelTanks,
        df.PrimaryFuelLevel,
        df.primaryFuelTankCapacity,
        df.SecondaryFuelLevel1,
        df.secondaryFuelTankCapacity1,
        df.defLevel,
        df.fuelLevelPercent,

        df.backupBatteryVoltage,
        df.vehicleBatteryVoltage,

        df.noOfBatteryPacks,

        json.dumps(df.batterySOC), 

        df.accelX,
        df.accelY,
        df.accelZ,
        df.gyroX,
        df.gyroY,
        df.gyroZ,

        df.engineRunHour,
        df.currentGear,

        df.eventDateTime
        
    )

    cursor.execute(query , values)
    conn.commit()

    cursor.close()
    conn.close()

    return ("vehicle data saved")



@app.get("/get-data" , status_code= status.HTTP_200_OK)

async def get_data():
    conn = connect()
    cursor = conn.cursor()

    query = "SELECT * FROM vehicle_telemetry.vehicle_telemetry;"
    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result



@app.get("/get-data-by-id{veh_id}"  , status_code= status.HTTP_200_OK)

async def getbyvehid(veh_id : str):
    conn = connect()
    cursor = conn.cursor()

    query = """
        SELECT * FROM vehicle_telemetry.vehicle_telemetry
        where vehicle_id = %s ;
    """
    cursor.execute(query , (veh_id,))

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

@app.put("/update-vehicle/{veh_id}")
def update_vehicle(veh_id: str, data: Dict[str , Any]= Body(...)):

    conn = None
    cursor = None

    try:
        conn = connect()
        cursor = conn.cursor()

        allowed_fields = [
            "speed",
            "fuelLevelPercent",
            "vehicleStatus",
            "engineRunHour",
            "currentGear"
        ]
        update_parts: list[str] = []
        values: list[Any] = []


        for key, value in data.items():
            if key in allowed_fields:

                column_name = key   

                if key == "fuelLevelPercent":
                    column_name = "fuel_level_percent"
                elif key == "vehicleStatus":
                    column_name = "vehicle_status"
                elif key == "engineRunHour":
                    column_name = "engine_run_hour"
                elif key == "currentGear":
                    column_name = "current_gear"
                else:
                    column_name = key

                update_parts.append(f"{column_name} = %s")
                values.append(value)


        if not update_parts:
            return {"message": "No valid fields provided"}

        query = f"""
        UPDATE vehicle_telemetry
        SET {", ".join(update_parts)}
        WHERE vehicle_id = %s
        """

        values.append(veh_id)

        cursor.execute(query, tuple(values))
        conn.commit()

        if cursor.rowcount == 0:
            return {"message": "Vehicle not found"}

        return {"message": "Vehicle updated successfully"}

    except Exception as e:
        return {"error": str(e)}

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



@app.delete("/del_data/{veh_id}"  , status_code= status.HTTP_200_OK)

async def delet_veh_data(veh_id : str):
    conn = connect()
    cursor = conn.cursor()

    query = """
        delete FROM vehicle_telemetry.vehicle_telemetry
        where vehicle_id = %s ;
    """

    cursor.execute(query , (veh_id,))
    conn.commit()

    cursor.close()
    conn.close()

