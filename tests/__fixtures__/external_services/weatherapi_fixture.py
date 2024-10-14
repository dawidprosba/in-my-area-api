import pytest
import requests_mock

from config import settings

api_key: str = settings.get("API_KEYS").get("weatherapi")
url: str = settings.get("WEATHERAPI").get("url")


@pytest.fixture(scope="session")
def weatherapi_alerts_mock():
    with requests_mock.Mocker() as mocker:
        mocker.get(
            url.format(api_key=api_key, endpoint="alerts", query="Cracow"),
            json={
                "location": {
                    "name": "Cracow",
                    "region": "",
                    "country": "Poland",
                    "lat": 50.0833,
                    "lon": 19.9167,
                    "tz_id": "Europe/Warsaw",
                    "localtime_epoch": 1728908672,
                    "localtime": "2024-10-14 14:24",
                },
                "alerts": {
                    "alert": [
                        {
                            "headline": "Flood Warning issued January 05 at 9:47PM...",
                            "msgtype": "Alert",
                            "severity": "Moderate",
                            "urgency": "Expected",
                            "areas": "Calhoun; Lexington; Richland",
                            "category": "Met",
                            "certainty": "Likely",
                            "event": "Flood Warning",
                            "note": "Alert for Calhoun; Lexington; Richland...",
                            "effective": "2021-01-05T21:47:00-05:00",
                            "expires": "2021-01-07T06:15:00-05:00",
                            "desc": "...The Flood Warning continues for the ...",
                            "instruction": "A Flood Warning means that flooding...",
                        },
                        {
                            "headline": "Flood Warning issued January 05 at 9:47PM...",
                            "msgtype": "Alert",
                            "severity": "Moderate",
                            "urgency": "Expected",
                            "areas": "Calhoun; Richland",
                            "category": "Met",
                            "certainty": "Likely",
                            "event": "Flood Warning",
                            "note": "Alert for Calhoun; Richland (South Caroli...",
                            "effective": "2021-01-05T21:47:00-05:00",
                            "expires": "2021-01-09T04:00:00-05:00",
                            "desc": "...The Flood Warning continues for th...",
                            "instruction": "A Flood Warning means that floo...",
                        },
                    ]
                },
            },
        )

        yield mocker
