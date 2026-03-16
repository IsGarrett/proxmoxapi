from fastapi import FastAPI
from endpoints.health import router as health_router
from endpoints.nodes import router as nodes_router


app = FastAPI()

app.include_router(health_router)
app.include_router(nodes_router)