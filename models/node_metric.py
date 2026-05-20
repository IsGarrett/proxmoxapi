from sqlalchemy import Column, Integer,BigInteger, String, Float, DateTime
from datetime import datetime
from db import Base

class NodeMetric(Base):
    __tablename__ = "node_metrics"

    id = Column(BigInteger, primary_key=True, index=True)
    node = Column(String, nullable=False)
    cpu = Column(Float)
    memory = Column(BigInteger)
    max_memory = Column(BigInteger)
    disk = Column(BigInteger)
    max_disk = Column(BigInteger)
    uptime = Column(Integer)
    status = Column(String)
    recorded_at = Column(DateTime, default=datetime.utcnow)