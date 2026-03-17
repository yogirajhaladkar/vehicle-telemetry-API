const mockVehicleData = [
    {
        vehicle: "MH12AB1234",
        date: "2026-03-16",
        time: "10:00",

        // 🔹 STATIC DATA (from your table image)
        staticData: {
            id: 1,
            vehicleId: "MH12AB1234",
            imei: "865412345678901",
            registrationNumber: "MH12AB1234",
            noOfFuelTanks: 1,
            primaryFuelTankCapacity: 50,
            secondaryFuelTankCapacity: 0,
            noOfBatteryPacks: 1
        },

        // 🔹 DYNAMIC DATA (telemetry)
        dynamicData: {
            id: 1,
            vehicleId: "MH12AB1234",
            latitude: 18.5204,
            longitude: 73.8567,
            altitude: 560,
            speed: 60,
            satellites: 4,
            ignition: 1,
            gpsFix: 1,
            gsmSignal: 1,
            rpm: 1200,
            odometer: 12000,
            fuelLevel: 30,
            fuelConsumption: 20,
            batteryVoltage: 12.4,
            batteryCurrent: 13.8,
            engineTemperature: 9.8,
            accelX: 0.001,
            accelY: 0.002,
            accelZ: 0.001,
            status: "Moving",
            tripDistance: 1250.5,
            gear: 3,
            avgSpeed: 60,
            tyrePressure: [78.5],
            timestamp: "10:00"
        }
    },

    {
        vehicle: "MH12AB1234",
        date: "2026-03-16",
        time: "10:05",

        staticData: {
            id: 1,
            vehicleId: "MH12AB1234",
            imei: "865412345678901",
            registrationNumber: "MH12AB1234",
            noOfFuelTanks: 1,
            primaryFuelTankCapacity: 50,
            secondaryFuelTankCapacity: 0,
            noOfBatteryPacks: 1
        },

        dynamicData: {
            id: 2,
            vehicleId: "MH12AB1234",
            latitude: 18.5210,
            longitude: 73.8575,
            altitude: 562,
            speed: 70,
            satellites: 5,
            ignition: 1,
            gpsFix: 1,
            gsmSignal: 1,
            rpm: 1400,
            odometer: 12010,
            fuelLevel: 28,
            fuelConsumption: 22,
            batteryVoltage: 12.5,
            batteryCurrent: 13.5,
            engineTemperature: 10.2,
            accelX: 0.002,
            accelY: 0.001,
            accelZ: 0.002,
            status: "Moving",
            tripDistance: 1255.0,
            gear: 4,
            avgSpeed: 65,
            tyrePressure: [78.2],
            timestamp: "10:05"
        }
    },

    {
        vehicle: "MH14XY5678",
        date: "2026-03-16",
        time: "10:00",

        staticData: {
            id: 2,
            vehicleId: "MH14XY5678",
            imei: "865498765432109",
            registrationNumber: "MH14XY5678",
            noOfFuelTanks: 2,
            primaryFuelTankCapacity: 60,
            secondaryFuelTankCapacity: 30,
            noOfBatteryPacks: 2
        },

        dynamicData: {
            id: 3,
            vehicleId: "MH14XY5678",
            latitude: 18.5300,
            longitude: 73.8500,
            altitude: 550,
            speed: 0,
            satellites: 3,
            ignition: 0,
            gpsFix: 1,
            gsmSignal: 1,
            rpm: 0,
            odometer: 8000,
            fuelLevel: 50,
            fuelConsumption: 0,
            batteryVoltage: 12.2,
            batteryCurrent: 12.8,
            engineTemperature: 8.5,
            accelX: 0.000,
            accelY: 0.000,
            accelZ: 0.000,
            status: "Idle",
            tripDistance: 800.0,
            gear: 0,
            avgSpeed: 0,
            tyrePressure: [80.0],
            timestamp: "10:00"
        }
    }
];

export default mockVehicleData;