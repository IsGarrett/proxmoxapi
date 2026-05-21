from fastapi import Depends, FastAPI, APIRouter
from services.auth import get_current_user
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
def start_lxc(vmid:int, current_user: str = Depends(get_current_user)):
    container = prox.nodes("homelab").lxc(vmid).status.start.post()
    return container

#stop lxc
@router.post('/v1/containers/{vmid}/stop')
def stop_vm(vmid:int, current_user: str = Depends(get_current_user)):
    container = prox.nodes("homeland").lxc(vmid).status.stop.post()
    return container