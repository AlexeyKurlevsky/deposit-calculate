import calendar
from datetime import datetime


def get_last_day_of_month(year: int, month: int) -> str:
    last_day = calendar.monthrange(year, month)[1]
    date = datetime(year, month, last_day)
    return date.strftime("%d.%m.%Y")
