from fastapi import FastAPI
from endpoints.health import router as health_router
from endpoints.nodes import router as nodes_router
from endpoints.virtual_machines import router as virtual_machine_router
from endpoints.containers import router as containers_router
from endpoints.auth import router as auth_router
from endpoints.ansible import router as services_router
from endpoints.audit_logs import router as audit_logs
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)


app.include_router(health_router)
app.include_router(nodes_router)
app.include_router(virtual_machine_router)
app.include_router(containers_router)
app.include_router(auth_router)
app.include_router(services_router)
app.include_router(audit_logs)

