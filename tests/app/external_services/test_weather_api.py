import pytest

from app.external_services.weather.fetchers.weatherapi_fetcher import WeatherAPIFetcher
from app.external_services.weather.models.weatherapi_alert_model import (
    WeatherAPIAlertModel,
)
from app.external_services.weather.weather_fetcher import WeatherFetcher


class TestWeatherApi:

    @pytest.mark.parametrize("city", ["Cracow"])
    def test_weatherapi_fetcher(self, weatherapi_alerts_mock, city):
        fetcher = WeatherAPIFetcher()

        alerts = fetcher.fetch_alerts(city=city)

        assert len(alerts) == 2
        assert type(alerts[0]) is WeatherAPIAlertModel

    def test_fetch_alerts_is_abstract(self):
        with pytest.raises(TypeError):
            WeatherFetcher()

        class Foo(WeatherFetcher):
            def fetch_alerts(self):
                super().fetch_alerts()

        with pytest.raises(NotImplementedError):
            Foo().fetch_alerts()
