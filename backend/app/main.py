from app.database.database import Base
from app.database.database import engine
from app.models.user_model import User
from fastapi import FastAPI
from app.api.user_api import router
from app.api.auth_api import router as auth_router


Base.metadata.create_all(

bind=engine
)
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

app.include_router(
auth_router,
prefix="/auth",
tags=["Authentication"]
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