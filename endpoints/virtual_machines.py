from fastapi import Depends, FastAPI, APIRouter
from services.auth import get_current_user
from services.proxmox import prox
from utils.parsers import parse_lxc_status, parse_node_response



router = APIRouter()


#get all VMs
@router.get('/v1/vms')
def get_all_vms(current_user: str = Depends(get_current_user)):

    all_vms = []
    nodes = prox.nodes.get()
    for node in nodes:
        vms = prox.nodes(node['node']).qemu.get()
        all_vms.extend(vms)
    return all_vms


#get specific VM's based off id passed in
@router.get('/v1/vms/{vmid}')
def get_vm(vmid: int, current_user: str = Depends(get_current_user)):
    vm = prox.nodes("homelab").qemu(vmid).status.current.get()
    return vm


#start vm
@router.post('/v1/vms/{vmid}/start')
def start_vm(vmid:int, current_user: str = Depends(get_current_user)):
    vm = prox.nodes("homelab").qemu(vmid).status.start.post()
    return vm

#stop vm
@router.post('/v1/vms/{vmid}/stop')
def stop_vm(vmid:int, current_user: str = Depends(get_current_user)):
    vm = prox.nodes("homeland").qemu(vmid).status.stop.post()
    return vm


