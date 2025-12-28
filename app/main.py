from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Lineage

app = FastAPI(title="Data Lineage Tracker")

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
