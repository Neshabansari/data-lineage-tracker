from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import engine, SessionLocal
from app.models import Base, Lineage


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Data Lineage Tracker")

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# STEP 6: API to get lineage
@app.get("/lineage/{dataset_id}")
def get_lineage(dataset_id: str, db: Session = Depends(get_db)):
    records = (
        db.query(Lineage)
        .filter(Lineage.dataset_id == dataset_id)
        .order_by(Lineage.timestamp)
        .all()
    )

    return [
        {
            "source": r.source,
            "operation": r.operation,
            "timestamp": r.timestamp
        }
        for r in records
    ]
