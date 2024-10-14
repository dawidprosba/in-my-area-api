from app.external_services.weather.weather_fetcher import WeatherAlertsFetcher


class WeatherAlerts:
    def __init__(self, api_fetcher: WeatherAlertsFetcher):
        self.fetcher = api_fetcher

    def get_alerts(self):
        return self.fetcher.fetch()
