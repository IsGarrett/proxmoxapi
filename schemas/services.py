from pydantic import BaseModel

class ServiceRequest(BaseModel):
    command: list