from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, field_validator


class WeatherAPIAlertModel(BaseModel):
    """
    Based on: https://www.weatherapi.com/docs/#apis-alerts
    """

    headline: str
    msg_type: str = Field(..., alias="msgtype")
    severity: str
    urgency: str
    areas: List[str]
    category: str
    certainty: str
    event: str
    note: str
    effective: datetime
    expires: datetime
    description: str = Field(..., alias="desc")
    instruction: str

    @field_validator("areas", mode="before")
    def areas_to_list(cls, v):
        return v.split("; ")
