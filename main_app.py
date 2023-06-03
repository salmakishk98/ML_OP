from fastapi import FastAPI
from main import multipl_xy

app = FastAPI()

@app.get("/")
def home():# end point 
    return "hello salme keep smile."

@app.get("/check")
def home123():
    return "OK, You are fine."

@app.get("/mul")
def mul_x_y_api(a:int, b:int):
    return multipl_xy(a, b)


