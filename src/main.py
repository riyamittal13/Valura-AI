from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from src.safety.guard import safety_check
from src.classifier.intent import classify
from src.router.router import route_query
import json
import time

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running"}


# 🔥 NEW: streaming function
def stream_response(data: dict):
    text = json.dumps(data)

    for char in text:
        yield char
        time.sleep(0.01)


@app.get("/query")
def query(q: str):
    # Step 1: Safety
    is_safe, message = safety_check(q)
    if not is_safe:
        return StreamingResponse(
            stream_response({"response": message}),
            media_type="text/event-stream"
        )

    # Step 2: Classifier
    # result = classify_intent(q)
    result = classify(q)

    # Step 3: Router → Agent
    # response = route_query(result["agent"], q)
    response = route_query(result.agent, q)

    # 🔥 Instead of return response
    return StreamingResponse(
        stream_response(response),
        media_type="text/event-stream"
    )