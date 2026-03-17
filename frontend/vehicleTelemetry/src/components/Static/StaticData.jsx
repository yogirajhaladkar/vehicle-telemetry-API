import { useSelector } from "react-redux";

export default function StaticData() {
    const staticData = useSelector((state) => state.vehicle.staticData);
    if (!staticData) {
        return <div className="p-4">No Data Found</div>;
    }
    return (
        <div className="p-4">
            {staticData && (
                <div>
                    <p><strong>Vehicle ID:</strong> {staticData.vehicleId}</p>
                    <p><strong>Registration Number:</strong> {staticData.registrationNumber}</p>
                    <p><strong>IMEI:</strong> {staticData.imei}</p>
                    <p><strong>No of Fuel Tanks:</strong> {staticData.noOfFuelTanks}</p>
                    <p><strong>Primary Tank Capacity:</strong> {staticData.primaryFuelTankCapacity}</p>
                    <p><strong>Secondary Tank Capacity:</strong> {staticData.secondaryFuelTankCapacity}</p>
                    <p><strong>Battery Packs:</strong> {staticData.noOfBatteryPacks}</p>
                </div>
            )}
        </div>
    )
}