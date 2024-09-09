from datetime import datetime

from pydantic import BaseModel, Field, StrictInt, field_validator


class DepositPayload(BaseModel):
    date: datetime = Field(examples=["31.01.2021"])
    periods: StrictInt = Field(ge=1, le=60)
    amount: StrictInt = Field(ge=10**3, le=3 * 10**6)
    rate: float = Field(ge=1, le=8)

    @field_validator("date", mode="before")
    @classmethod
    def validate_end_date(cls, value: str) -> datetime:
        try:
            res = datetime.strptime(value, "%d.%m.%Y")
        except ValueError as error:
            raise ValueError("Неверно указан формат даты. Укажите в формате dd.mm.YYYY") from error

        return res
