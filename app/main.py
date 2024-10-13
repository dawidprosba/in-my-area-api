from fastapi import FastAPI

app = FastAPI()

# app.include_router(endpoints.router)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
