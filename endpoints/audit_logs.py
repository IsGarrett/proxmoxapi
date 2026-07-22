

from typing import Annotated
from fastapi import Depends, FastAPI, APIRouter, Query
from requests import Session
from db import get_db
from models.user import User
from services.database import list_audit_logs, resource_type
from services.auth import get_current_user
from services.proxmox import prox
from utils.parsers import parse_lxc_status, parse_node_response
from models.audit import AuditLog
from schemas.audit_log import AuditLogResponse


router = APIRouter()


@router.get("/v1/audit", response_model=list[AuditLogResponse])
def list_audit_logs_service(
    query_limit: Annotated[int, Query(ge=1, le=100)] = 15,
    offset: Annotated[int, Query(ge=0)] = 0,
    resource_type: str | None = None,
    current_user: str = Depends(get_current_user),
    db = Depends(get_db)
):
    
    return list_audit_logs(query_limit, offset, db)


