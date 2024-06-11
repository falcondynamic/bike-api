from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get('/prediction/{param1}/{param2}/{param3}/{param4}/{param5}/{param6}')
def prediction(param1: int, param2: int, param3: str, param4: int, param5: str, param6: str):
    return {"message": f"Prediction! {param1}, {param2}, {param3}, {param4}, {param5}, {param6}"}