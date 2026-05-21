from sqlalchemy import Boolean, Column, Integer, BigInteger, String, Float, DateTime
from datetime import datetime
from db import Base


class User(Base):
    __tablename__ = 'user_logins'

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String,unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)