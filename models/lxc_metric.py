from sqlalchemy import Column, Integer, BigInteger, String, Float, DateTime
from datetime import datetime
from db import Base


class LxcMetric(Base):
    __tablename__ = 'lxc_metrics'

    id = Column(BigInteger, primary_key=True, index=True)
    vmid = Column(Integer)
    name = Column(String, nullable=False)
    status = Column(String)
    cpu = Column(Float)
    memory = Column(BigInteger)
    recorded_at = Column(DateTime, default=datetime)

