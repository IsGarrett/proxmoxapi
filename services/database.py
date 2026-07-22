from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db

from models.audit import AuditLog

from models.user import User
from services.auth import get_current_user, hash_password, verify_password, create_access_token, decode_token




def list_audit_logs(query_limit, offset, db, resource_type=None):
    query = db.query(AuditLog)
    
    if resource_type:
        query = query.filter(AuditLog.resource_type == resource_type)
    
    return query.order_by(AuditLog.created_at.desc()).limit(query_limit).offset(offset).all()

def resource_type(db: Session, resource_type: str, query_limit: int, off_set: int) -> list[AuditLog]:
    return (
        db.query(AuditLog)
        .filter(AuditLog.resource_type == resource_type)
        .order_by(AuditLog.created_at.desc())
        .limit(query_limit)
        .offset(off_set)
        .all()
    )

def log_action(db: Session, action, resource_type, resource_id, status, detail):

    log = AuditLog(
        action = action,
        resource_type=resource_type,
        resource_id=resource_id,
        status=status, 
        detail=detail
    )
    db.add(log)
    db.commit()
    db.refresh(log)
