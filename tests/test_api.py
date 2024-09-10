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
            "31.05.2021": 10252.51,
            "30.06.2021": 10303.78,
            "31.07.2021": 10355.29,
        }
    )
    assert response.json() == target


def test_next_year():
    request_payload = {"date": "31.12.2022", "periods": 7, "amount": 10000, "rate": 6}
    response = client.post("/calculate", json=request_payload)
    assert response.status_code == 200
    target = OrderedDict(
        {
            "31.12.2022": 10050,
            "30.01.2023": 10100.25,
            "29.02.2023": 10150.75,
            "31.03.2023": 10201.51,
            "30.04.2023": 10252.51,
            "30.05.2023": 10303.78,
            "31.06.2023": 10355.29,
        }
    )
    assert response.json() == target

    leap_year = {"date": "31.12.2023", "periods": 7, "amount": 10000, "rate": 6}
    response = client.post("/calculate", json=leap_year)
    assert response.status_code == 200
    target = OrderedDict(
        {
            "31.12.2023": 10050,
            "30.01.2024": 10100.25,
            "29.02.2024": 10150.75,
            "31.03.2024": 10201.51,
            "30.04.2024": 10252.51,
            "30.05.2024": 10303.78,
            "31.06.2024": 10355.29,
        }
    )
    assert response.json() == target
