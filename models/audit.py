from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(String, nullable=False)
    resource_type = Column(String, nullable=False)
    resource_id = Column(String)
    status = Column(String)
    detail = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)