from fastapi import FastAPI
from endpoints.health import router as health_router
from endpoints.nodes import router as nodes_router
from endpoints.virtual_machines import router as virtual_machine_router


app = FastAPI()

app.include_router(health_router)
app.include_router(nodes_router)
app.include_router(virtual_machine_router)