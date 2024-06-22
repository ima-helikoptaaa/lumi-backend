from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def starter():
    return {"message": "starter"}
