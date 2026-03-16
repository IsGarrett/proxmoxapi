from pydantic import BaseModel

class LXCResponse(BaseModel):
    vmid: int
    name: str
    status: str
    cpu: float
    memory: int