from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class Lineage(Base):
    __tablename__ = "lineage"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(String, index=True)
    source = Column(String)
    operation = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
