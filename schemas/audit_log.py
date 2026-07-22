from pydantic import BaseModel
from datetime import datetime


class AuditLogResponse(BaseModel):
    action: str
    resource_type: str
    resource_id: str
    status: str
    detail: str
    created_at: datetime