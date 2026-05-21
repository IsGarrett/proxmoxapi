from fastapi import Depends, FastAPI, APIRouter
from services.auth import get_current_user
from services.proxmox import prox
from utils.parsers import parse_lxc_status, parse_node_response



router = APIRouter()


#get container health
@router.get('/v1/nodes/lxc/{vmid}')
def get_lxc(vmid: int, current_user: str = Depends(get_current_user)):
    raw = prox.nodes("homelab").lxc(vmid).status.current.get()
    return parse_lxc_status(raw)


#get nodes using parser
@router.get('/v1/nodes')
def get_nodes(current_user: str = Depends(get_current_user)):
    nodes = prox.nodes.get()
    return [parse_node_response(node) for node in nodes]


    
