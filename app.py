import os
from fastapi import FastAPI
import uvicorn

# 1. Initialize the API
app = FastAPI()

# 2. The Core Logic (The Brain)
def add(a, b):
    return a + b

# 3. The API Endpoint (The Reception Desk)
@app.get("/")
def home():
    return {"status": "System Online", "message": "Welcome to the Technocrat API"}

@app.get("/predict")
def predict_math(a: int, b: int):
    # The outside world asks for a prediction
    result = add(a, b)
    # We return the answer in JSON (Universal Language)
    return {"input": [a, b], "prediction": result}

# 4. The Launch Protocol
if __name__ == "__main__":
    # CRITICAL FIX: Get the PORT from Render. 
    # If Render doesn't give one (like on your laptop), default to 8080.
    port = int(os.environ.get("PORT", 8080))
    
    # Run the server on 0.0.0.0 so the cloud can find it.
    uvicorn.run(app, host="0.0.0.0", port=port)
