from fastapi import FastAPI, HTTPException
import os
import psycopg2
import psycopg2.extras
from datetime import datetime

app = FastAPI(title="Demo API", version="1.0.3")


# --- Health endpoint ---
@app.get("/health")
def health():
    return {"status": "ok"}


# --- Items endpoint ---
@app.get("/items")
def get_items():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute("SELECT id, name, price FROM items ORDER BY id;")
        rows = cursor.fetchall()
        return {"items": [dict(row) for row in rows]}
    finally:
        conn.close()


# --- Database connection helper ---
def get_db_connection():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise HTTPException(status_code=500, detail="DATABASE_URL not set")
    return psycopg2.connect(database_url)


# --- Version endpoint ---
@app.get("/version")
def version():
    return {
        "version":     os.getenv("APP_VERSION", "dev"),
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "service":     "backend-api"
    }


# --- Root endpoint ---
# Added server_time — small change to trigger CI pipeline
@app.get("/")
def root():
    return {
        "service":     "backend-api",
        "version":     os.getenv("APP_VERSION", "dev"),
        "docs":        "/docs",
        "server_time": datetime.utcnow().isoformat()
    }