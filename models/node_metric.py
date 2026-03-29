from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from db import Base

class NodeMetric(Base):
    __tablename__ = "node_metrics"

    id = Column(Integer, primary_key=True, index=True)
    node = Column(String, nullable=False)
    cpu = Column(Float)
    memory = Column(Integer)
    max_memory = Column(Integer)
    disk = Column(Integer)
    max_disk = Column(Integer)
    uptime = Column(Integer)
    status = Column(String)
    recorded_at = Column(DateTime, default=datetime.utcnow)