class TestWeatherRouter:
    def test_get_alerts(self, api_client, weatherapi_alerts_mock):
        response = api_client.get("/weather/alerts?city=Cracow")

        assert response.status_code == 200

        data = response.json()

        assert data["count"] == 2
