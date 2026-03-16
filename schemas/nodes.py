from pydantic import BaseModel

class NodeResponse(BaseModel):
    uptime: int
    node: str
    maxcpu: int
    status: str
    cpu: float
    disk: int
