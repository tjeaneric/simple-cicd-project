from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome_message():
    return {"message": "Welcome to the Testing API!"}
