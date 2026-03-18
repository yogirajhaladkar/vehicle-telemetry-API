import { useSelector } from "react-redux";

export default function DynamicData() {
    const dynamicData = useSelector((state) => state.vehicle.dynamicData);

    if (!dynamicData) {
        return <div className="p-8">No Data Found</div>;
    }

    return (
        <div className=" p-8">
            <h2 className="font-bold mb-2">Dynamic Data</h2>


            {/* <p><strong>Latitude:</strong> {dynamicData.latitude}</p>
            <p><strong>Longitude:</strong> {dynamicData.longitude}</p> */}
            <p><strong>Altitude:</strong> {dynamicData.altitude}</p>


            <p><strong>Speed:</strong> {dynamicData.speed} km/h</p>
            <p><strong>Status:</strong> {dynamicData.status}</p>
            <p><strong>Gear:</strong> {dynamicData.gear}</p>
            <p><strong>Avg Speed:</strong> {dynamicData.avgSpeed}</p>

            <p><strong>RPM:</strong> {dynamicData.rpm}</p>
            <p><strong>Ignition:</strong> {dynamicData.ignition}</p>
            <p><strong>GPS Fix:</strong> {dynamicData.gpsFix}</p>
            <p><strong>GSM Signal:</strong> {dynamicData.gsmSignal}</p>
            <p><strong>Satellites:</strong> {dynamicData.satellites}</p>

            <p><strong>Fuel Level:</strong> {dynamicData.fuelLevel}%</p>
            <p><strong>Fuel Consumption:</strong> {dynamicData.fuelConsumption}</p>

            <p><strong>Battery Voltage:</strong> {dynamicData.batteryVoltage}</p>
            <p><strong>Battery Current:</strong> {dynamicData.batteryCurrent}</p>

            <p><strong>Engine Temperature:</strong> {dynamicData.engineTemperature}</p>

            <p><strong>Accel X:</strong> {dynamicData.accelX}</p>
            <p><strong>Accel Y:</strong> {dynamicData.accelY}</p>
            <p><strong>Accel Z:</strong> {dynamicData.accelZ}</p>

            <p><strong>Trip Distance:</strong> {dynamicData.tripDistance}</p>
            <p><strong>Odometer:</strong> {dynamicData.odometer}</p>

            <p><strong>Tyre Pressure:</strong> {dynamicData.tyrePressure?.join(", ")}</p>


            <p><strong>Timestamp:</strong> {dynamicData.timestamp}</p>
        </div>
    );
}