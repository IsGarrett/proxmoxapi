from fastapi import FastAPI, APIRouter
from services.proxmox import prox
from utils.parsers import parse_lxc_status
from sqlalchemy import text
from db import engine

router = APIRouter()


#Checks API is running
@router.get('/health')
def health():
    return {"status": "ok"}


#get node health
@router.get('/health/nodes')
def get_node_health():
    try:
        nodes = prox.nodes.get()
        return {'status':'ok', 'nodes': len(nodes)}
    except Exception as e:
        return {'status':'error', 'detail': str(e)}

#db health check
@router.get('/health/db')
def db_health():
    try:
        with engine.connect() as conn:
            conn.execute(text('SELECT 1'))
        return {'status': 'ok'}
    except Exception as e:
        return {'status': 'error', 'detail': str(e)}
    

    


