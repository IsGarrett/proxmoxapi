from fastapi import FastAPI, APIRouter
from services.proxmox import prox
from utils.parsers import parse_lxc_status, parse_node_response



router = APIRouter()


#get all VMs
@router.get('/v1/vms')
def get_all_vms():

    all_vms = []
    nodes = prox.nodes.get()
    for node in nodes:
        vms = prox.nodes(node['node']).qemu.get()
        all_vms.extend(vms)
    return all_vms

#get specific VM's based off id passed in
@router.get('/v1/vms/{vmid}')
def get_vm(vmid: int):
    vm = prox.nodes("homelab").qemu(vmid).status.current.get()
    return vm
