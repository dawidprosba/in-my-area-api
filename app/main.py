from fastapi import FastAPI

from app.routers import weather_router

app = FastAPI()


app.include_router(weather_router, prefix="/weather")


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
