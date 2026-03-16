from fastapi import FastAPI, APIRouter
from services.proxmox import prox
from utils.parsers import parse_lxc_status, parse_node_response



router = APIRouter()


#get container health
@router.get('/v1/nodes/lxc/{vmid}')
def get_lxc(vmid: int):
    raw = prox.nodes("homelab").lxc(vmid).status.current.get()
    return parse_lxc_status(raw)


#get nodes using parser
@router.get('/v1/nodes')
def get_nodes():
    nodes = prox.nodes.get()
    return [parse_node_response(node) for node in nodes]


    
