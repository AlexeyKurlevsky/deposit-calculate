from collections import OrderedDict
from decimal import Decimal
from pathlib import Path

from fastapi import APIRouter
from starlette.responses import PlainTextResponse
from tomllib import load as load_toml

from api.data_models import DepositPayload, ResponseModel
from api.utils import get_last_day_of_month


routes = APIRouter()


@routes.post("/calculate")
async def calculate_deposit(payload: DepositPayload) -> ResponseModel:
    values = OrderedDict()

    amount = payload.amount
    year = payload.date.year
    month = payload.date.month
    for _ in range(1, payload.periods + 1):
        initial_date = get_last_day_of_month(year, month)
        amount *= 1 + Decimal(payload.rate / 12 / 100)
        amount = Decimal(amount).quantize(Decimal("1.00"))
        values[initial_date] = amount

        month += 1
        if month > 12:
            month = 1
            year += 1

    return ResponseModel(root=values)


@routes.get("/version")
async def api_get_version() -> PlainTextResponse:
    with Path("pyproject.toml").open("rb") as pyproject_file:
        parsed_pyproject = load_toml(pyproject_file)

    version = parsed_pyproject["tool"]["poetry"]["version"]

    return PlainTextResponse(version)
