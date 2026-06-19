from fastapi import FastAPI

app = FastAPI(
    title="SmartCreditAI",
    description="AI Powered Loan Risk Assessment Platform",
    version="1.0"
)


@app.get("/")
def home():

    return {

        "message":"Welcome to SmartCreditAI"

    }


@app.get("/health")

def health():

    return {

        "status":"running"

    }