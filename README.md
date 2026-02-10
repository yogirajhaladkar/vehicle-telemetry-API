# 🚗 Vehicle Telemetry Backend API

A backend API built using **FastAPI** and **MySQL** for managing vehicle telemetry data.

This project supports full **CRUD operations** and allows dynamic field updates for vehicle records.

---

## 📌 Features

- Insert vehicle telemetry data
- Get all vehicle records
- Get vehicle data by ID
- Update multiple fields dynamically
- Delete vehicle records
- JSON payload support
- MySQL database integration

---

## 🛠️ Tech Stack

- Python
- FastAPI
- MySQL
- Pydantic
- Uvicorn

---

## 📂 API Endpoints

### 🔹 Insert Data
`POST /post_vehivcle_update`

Inserts a new vehicle telemetry record.

---

### 🔹 Get All Data
`GET /get-data`

Returns all vehicle telemetry records.

---

### 🔹 Get Data By Vehicle ID
`GET /get-data-by-id/{veh_id}`

Returns telemetry data for a specific vehicle.

---

### 🔹 Update Vehicle Data
`PUT /update-vehicle/{veh_id}`

Allows dynamic update of selected fields.

Example body:
```json
{
  "speed": 100,
  "vehicleStatus": "Running"
}
