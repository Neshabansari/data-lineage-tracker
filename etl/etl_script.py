import pandas as pd
from datetime import datetime
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Lineage


# Function to log lineage records
def log_lineage(dataset_id, source, operation):
    db: Session = SessionLocal()
    record = Lineage(
        dataset_id=dataset_id,
        source=source,
        operation=operation,
        timestamp=datetime.utcnow()
    )
    db.add(record)
    db.commit()
    db.close()


# STEP 1: Extract
df = pd.read_csv("data/sales.csv")
log_lineage("sales_v1", "sales.csv", "Loaded raw data")


# STEP 2: Transform - remove null values
df = df.dropna()
log_lineage("sales_v2", "sales.csv", "Removed null values")


# STEP 3: Transform - filter year = 2024
df = df[df["year"] == 2024]
log_lineage("sales_v3", "sales.csv", "Filtered data for year 2024")


# STEP 4: Load - save final dataset
df.to_csv("data/final_sales.csv", index=False)
log_lineage("sales_final", "sales.csv", "Saved cleaned dataset")

def run_etl():
    log_lineage("sales_v1", "sales.csv", "Loaded raw data")
    log_lineage("sales_v2", "sales.csv", "Removed null values")
    log_lineage("sales_v3", "sales.csv", "Filtered data for year 2024")
    log_lineage("sales_final", "sales.csv", "Saved cleaned dataset")

