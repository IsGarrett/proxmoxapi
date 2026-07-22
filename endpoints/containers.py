from fastapi import Depends, FastAPI, APIRouter
from db import get_db
from services.auth import get_current_user
from services.database import log_action
from services.proxmox import prox
from utils.parsers import parse_lxc_status, parse_node_response



router = APIRouter()


#get all containers
@router.get('/v1/containers')
def get_containers(current_user: str = Depends(get_current_user)):
    containers = prox.nodes("homelab").lxc.get()
    return [parse_lxc_status(container) for container in containers]

#get specific container
@router.get('/v1/containers/{vmid}')
def get_container(vmid: int, current_user: str = Depends(get_current_user)):
    container = prox.nodes("homelab").lxc(vmid).status.current.get()
    return parse_lxc_status(container)

#start lxc
@router.post('/v1/containers/{vmid}/start')
def start_lxc(vmid:int, current_user: str = Depends(get_current_user), db = Depends(get_db)):
    container = prox.nodes("homelab").lxc(vmid).status.start.post()
    log_action(db, action='start-container', resource_type='lxc', resource_id=vmid, status='success',detail=f'LXC {vmid} started..')
    return container

#stop lxc
@router.post('/v1/containers/{vmid}/stop')
def stop_vm(vmid:int, current_user: str = Depends(get_current_user), db = Depends(get_db)):
    container = prox.nodes("homelab").lxc(vmid).status.stop.post()
    log_action(db, action='stop-lxc', resource_type='lxc', resource_id=vmid, status='success',detail=f'VM {vmid} stopped..')
    return container