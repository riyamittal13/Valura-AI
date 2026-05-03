# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Server is running"}


from fastapi import FastAPI
from src.safety.guard import safety_check

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running"}

@app.get("/query")
def query(q: str):
    is_safe, message = safety_check(q)

    if not is_safe:
        return {"response": message}

    return {"response": "Query is safe, processing..."}