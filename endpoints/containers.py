from fastapi import FastAPI, APIRouter
from services.proxmox import prox
from utils.parsers import parse_lxc_status, parse_node_response



router = APIRouter()


#get all containers
@router.get('/v1/containers')
def get_containers():
    containers = prox.nodes("homelab").lxc.get()
    return [parse_lxc_status(container) for container in containers]

#get specific container
@router.get('/v1/containers/{vmid}')
def get_container(vmid: int):
    container = prox.nodes("homelab").lxc(vmid).status.current.get()
    return parse_lxc_status(container)

#start lxc
@router.post('/v1/containers/{vmid}/start')
def start_lxc(vmid:int):
    container = prox.nodes("homelab").lxc(vmid).status.start.post()
    return container

#stop lxc
@router.post('/v1/containers/{vmid}/stop')
def stop_vm(vmid:int):
    container = prox.nodes("homeland").lxc(vmid).status.stop.post()
    return container