import os
import time

from fastapi import FastAPI

START_TIME = time.time()

app = FastAPI(title="Portfolio API")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/api/about")
def about():
    return {
        "pod": os.getenv("HOSTNAME", "unknown"),
        "version": os.getenv("GIT_SHA", "dev"),
        "uptime_seconds": int(time.time() - START_TIME),
    }
