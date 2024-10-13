class TestMain:
    def test_read_root(self, api_client):
        response = api_client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, FastAPI!"}
