import sys
from collections import OrderedDict


sys.path.append("./src")


from fastapi.testclient import TestClient

from main import init_app


client = TestClient(init_app())


def test_result_calculate():
    request_payload = {"date": "31.01.2021", "periods": 7, "amount": 10000, "rate": 6}
    response = client.post("/calculate", json=request_payload)
    assert response.status_code == 200
    target = OrderedDict(
        {
            "31.01.2021": 10050,
            "28.02.2021": 10100.25,
            "31.03.2021": 10150.75,
            "30.04.2021": 10201.51,
            "30.06.2021": 10303.78,
            "31.07.2021": 10355.29,
        }
    )
    assert response.json() == target
