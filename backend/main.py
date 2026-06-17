from fastapi import FastAPI
import os

app = FastAPI(title="Demo API", version="1.0.1")


# --- Health endpoint ---
# Kubernetes liveness and readiness probes call this.
@app.get("/health")
def health():
    return {"status": "ok"}


# --- Items endpoint ---
# In-memory data for now — wired to PostgreSQL in Stage 4.
ITEMS = [
    {"id": 1, "name": "widget",    "price": 9.99},
    {"id": 2, "name": "gadget",    "price": 24.99},
    {"id": 3, "name": "doohickey", "price": 4.99},
]

@app.get("/items")
def get_items():
    return {"items": ITEMS}


# --- Version endpoint --- NEW in v1.0.1
# Shows which version is running — useful to verify a deployment worked.
# In production you'd use this to confirm the new image is live
# without having to check pod logs or kubectl describe.
@app.get("/version")
def version():
    return {
        "version":     os.getenv("APP_VERSION", "dev"),
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "service":     "backend-api"
    }


# --- Root endpoint ---
@app.get("/")
def root():
    return {
        "service": "backend-api",
        "version": os.getenv("APP_VERSION", "dev"),
        "docs":    "/docs"
    }