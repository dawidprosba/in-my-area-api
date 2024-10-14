from typing import List

import requests
from pydantic import TypeAdapter

from app.external_services.weather.models.weatherapi_alert_model import (
    WeatherAPIAlertModel,
)
from app.external_services.weather.weather_fetcher import WeatherFetcher
from config import settings


class WeatherAPIFetcher(WeatherFetcher):
    _api_key: str = settings.get("API_KEYS").get("weatherapi")
    _base_url: str = settings.get("WEATHERAPI", {}).get("url")

    def fetch_alerts(self, city: str) -> List[WeatherAPIAlertModel]:
        url = self._base_url.format(
            api_key=self._api_key, endpoint="alerts", query=city
        )

        data = requests.get(url).json()

        alerts = data.get("alerts", {}).get("alert", [])
        # Create a TypeAdapter for List[Item]
        adapter = TypeAdapter(List[WeatherAPIAlertModel])

        return adapter.validate_python(alerts)
