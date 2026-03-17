import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

export const fetchVehicleData = createAsyncThunk(
  "vehicle/fetchVehicleData",
  async ({ vehicle, date, time }, thunkAPI) => {
    try {
      const formattedTime = time.length === 5 ? `${time}:00` : time;

      const response = await fetch(
        `http://127.0.0.1:8000/gps/vehicle/${vehicle}/telemetry?date=${date}&time=${formattedTime}`
      );

      if (!response.ok) {
        throw new Error("Failed to fetch vehicle data");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      return thunkAPI.rejectWithValue(error.message);
    }
  }
);

const initialState = {
  filter: {
    vehicle: "",
    date: "",
    time: "",
  },
  staticData: null,
  dynamicData: null,
  loading: false,
  error: null,
};

const vehicleSlice = createSlice({
  name: "vehicle",
  initialState,
  reducers: {
    setFilter: (state, action) => {
      state.filter = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchVehicleData.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchVehicleData.fulfilled, (state, action) => {
        state.loading = false;
        state.staticData = action.payload.staticData;
        state.dynamicData = action.payload.dynamicData;
      })
      .addCase(fetchVehicleData.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload || "Something went wrong";
      });
  },
});

export const { setFilter } = vehicleSlice.actions;
export default vehicleSlice.reducer;