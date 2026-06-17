from fastapi import FastAPI
import os

# FastAPI is like Flask but better for APIs.
# It auto-generates a Swagger UI at /docs — no extra work needed.
# You can open /docs in a browser and test every endpoint interactively.
app = FastAPI(title="Demo API", version="1.0.0")


# --- Health endpoint ---
# Kubernetes calls this to check if the pod is alive and ready.
# If this returns 200 = pod is healthy, send it traffic.
# If this fails = Kubernetes restarts the pod automatically.
# Equivalent to a Target Group health check on an AWS ALB.
@app.get("/health")
def health():
    return {"status": "ok"}


# --- Items endpoint ---
# Returns a hardcoded list for now.
# In Stage 4 we replace this with a real PostgreSQL query.
# Think of this as a mock DynamoDB scan for now.
ITEMS = [
    {"id": 1, "name": "widget",    "price": 9.99},
    {"id": 2, "name": "gadget",    "price": 24.99},
    {"id": 3, "name": "doohickey", "price": 4.99},
]

@app.get("/items")
def get_items():
    return {"items": ITEMS}


# --- Root endpoint ---
# Returns basic service info — useful for debugging.
# APP_VERSION is injected by Helm at deploy time via an environment variable.
# Think of it like an SSM Parameter Store value being injected into a Lambda.
@app.get("/")
def root():
    return {
        "service": "backend-api",
        "version": os.getenv("APP_VERSION", "dev"),
        "docs":    "/docs"
    }