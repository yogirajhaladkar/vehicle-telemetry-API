import { use, useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { setFilter, fetchVehicleData } from "../../store/vehicleSlice";

const generateTimeOptions = () => {
  const options = [];
  for (let h = 0; h < 24; h++) {
    for (let m = 0; m < 60; m += 5) {
      const time = `${h.toString().padStart(2, "0")}:${m
        .toString()
        .padStart(2, "0")}`;
      options.push(time);
    }
  }
  return options;
};

const timeOptions = generateTimeOptions();

export default function Filter() {
  const dispatch = useDispatch();

  const [vehicle, setVehicle] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");
  const [vehicles, setVehicles] = useState([]);
  const [timeOptions, setTimeOptions] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/vehicles")
      .then(res => res.json())
      .then(data => setVehicles(data));
  }, []);

  useEffect(() => {
    if (vehicle && date) {
      fetch(`http://127.0.0.1:8000/times/vehicle/${vehicle}/${date}`)
        .then(res => res.json())
        .then(data => setTimeOptions(data));
    }
  }, [vehicle, date]);


  const handleFilter = () => {
    const filterData = { vehicle, date, time };

    dispatch(setFilter(filterData));
    dispatch(fetchVehicleData(filterData));
  };

  return (
    <div className="flex flex-row justify-around p-4">
      <select
        className="border-2 border-gray-300 px-4 py-2 m-2 rounded"
        value={vehicle}
        onChange={(e) => setVehicle(e.target.value)}
      >
        <option value="">Select Vehicle</option>
        {vehicles.map((v) => (
          <option key={v} value={v}>
            {v}
          </option>
        ))}
      </select>

      <input
        className="border-2 border-gray-300 px-4 py-2 m-2 rounded"
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />

      <select
        className="border-2 border-gray-300 px-4 py-2 m-2 rounded"
        value={time}
        onChange={(e) => setTime(e.target.value)}
      >
        <option value="">Select Time</option>
        {timeOptions.map((time, index) => (
          <option key={index} value={time}>
            {time}
          </option>
        ))}
      </select>

      <button
        onClick={handleFilter}
        className="border-2 hover:bg-gray-300 m-2 border-gray-300 px-4 py-2 rounded"
      >
        Filter
      </button>
    </div>
  );
}