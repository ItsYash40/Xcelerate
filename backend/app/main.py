from fastapi import FastAPI

from app.api.user_api import router

app=FastAPI(
title="SmartCreditAI",
description="AI Powered Loan Risk Assessment Platform",
version="1.0"
)

app.include_router(
router,
prefix="/user",
tags=["User"]
)

@app.get("/")

def home():
    return {
        "message":
        "Welcome to SmartCreditAI"
    }

@app.get("/health")
def health():
    return {
        "status":"running"
    }