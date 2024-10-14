from abc import ABC, abstractmethod


class WeatherFetcher(ABC):
    @abstractmethod
    def fetch_alerts(self):
        raise NotImplementedError
