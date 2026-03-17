import { configureStore } from "@reduxjs/toolkit";
import vehicleReducer from "./VehicleSlice";

export const store = configureStore({
    reducer: {
        vehicle: vehicleReducer
    }
});