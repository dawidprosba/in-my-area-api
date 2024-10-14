from fastapi import APIRouter

from app.external_services.weather.fetchers.weatherapi_fetcher import WeatherAPIFetcher

router = APIRouter()


@router.get("/alerts/")
async def get_alerts(city: str):
    alerts = WeatherAPIFetcher().fetch_alerts(city)

    return {
        "count": len(alerts),
        "alerts": alerts,
    }
