from fastapi.testclient import TestClient
from main import app
import json
import time
import pytest
from typing import Any

client = TestClient(app)

with open("test/data.json") as f:
    VehData = json.load(f)

@pytest.mark.parametrize("Data" , VehData)

def test_newlocation(Data :Any):
        rsp = client.post("/gps/new-location" , json= Data["data"])
        
        assert rsp.status_code==Data["expected_status"]
        time.sleep(1)  




