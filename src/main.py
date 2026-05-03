# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Server is running"}


# from fastapi import FastAPI
# from src.safety.guard import safety_check

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Server is running"}

# @app.get("/query")
# def query(q: str):
#     is_safe, message = safety_check(q)

#     if not is_safe:
#         return {"response": message}

#     return {"response": "Query is safe, processing..."}

from fastapi import FastAPI
from src.safety.guard import safety_check
from src.classifier.intent import classify_intent

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running"}

@app.get("/query")
def query(q: str):
    # Step 1: Safety check
    is_safe, message = safety_check(q)
    if not is_safe:
        return {"response": message}

    # Step 2: Classification
    result = classify_intent(q)

    return {
        "intent": result["intent"],
        "agent": result["agent"]
    }