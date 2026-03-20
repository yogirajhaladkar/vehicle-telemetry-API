import { useSelector } from "react-redux";

export default function DynamicData() {
    const dynamicData = useSelector((state) => state.vehicle.dynamicData);

    if (!dynamicData) {
        return <div className="p-8">No Data Found</div>;
    }

    return (
        <div className=" p-8">
            <p><strong>Altitude:</strong> {dynamicData.altitude}</p>
            <p><strong>GPS Course In Degrees:</strong> {dynamicData.gps_CourseInDegrees}</p>
            <p><strong>GPS Signal Quality:</strong> {dynamicData.gps_SignalQuality}</p>
            <p><strong>GPS Fix:</strong> {dynamicData.gpsFix ? "Yes" : "No"}</p>
            <p><strong>Ignition:</strong> {dynamicData.ignition ? "On" : "Off"}</p>
            <p><strong>Crank:</strong> {dynamicData.crank ? "On" : "Off"}</p>
            <p><strong>Speed:</strong> {dynamicData.speed} km/h</p>
            <p><strong>Odometer:</strong> {dynamicData.odometer}</p>
            <p><strong>Primary Fuel Level:</strong> {dynamicData.primaryFuelLevel}</p>
            <p><strong>Secondary Fuel Level 1:</strong> {dynamicData.secondaryFuelLevel1}</p>
            <p><strong>DEF Level:</strong> {dynamicData.defLevel}</p>
            <p><strong>Backup Battery Voltage:</strong> {dynamicData.backupBatteryVoltage}</p>
            <p><strong>Battery Voltage:</strong> {dynamicData.batteryVoltage}</p>
            <p><strong>Accel X:</strong> {dynamicData.accelX}</p>
            <p><strong>Accel Y:</strong> {dynamicData.accelY}</p>
            <p><strong>Accel Z:</strong> {dynamicData.accelZ}</p>
            <p><strong>Gyro X:</strong> {dynamicData.gyroX}</p>
            <p><strong>Gyro Y:</strong> {dynamicData.gyroY}</p>
            <p><strong>Gyro Z:</strong> {dynamicData.gyroZ}</p>
            <p><strong>AC Status:</strong> {dynamicData.status}</p>
            <p><strong>Vehicle Status:</strong> {dynamicData.vehicleStatus}</p>
            <p><strong>Engine Run Hour:</strong> {dynamicData.engineRunHour}</p>
            <p><strong>Gear:</strong> {dynamicData.gear}</p>
            <p><strong>Fuel Level Percent:</strong> {dynamicData.fuelLevelPercent}%</p>
            <p><strong>Battery SOC:</strong> {dynamicData.batterySOC}</p>
            <p><strong>Timestamp:</strong> {dynamicData.timestamp}</p>
        </div>
    );
}