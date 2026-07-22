from fastapi import Depends, FastAPI, APIRouter, HTTPException
from services.auth import get_current_user
from services.proxmox import prox
from utils.parsers import parse_lxc_status, parse_node_response
from services.database import log_action
from db import get_db





router = APIRouter()


#get all VMs
@router.get('/v1/vms')
def get_all_vms(current_user: str = Depends(get_current_user)):

    all_vms = []
    nodes = prox.nodes.get()
    
    if nodes is None:
        raise HTTPException(status_code=404, detail="All VM's not found!")

    for node in nodes:
        vms = prox.nodes(node['node']).qemu.get()
        all_vms.extend(vms)
    return all_vms


#get specific VM's based off id passed in
@router.get('/v1/vms/{vmid}')
def get_vm(vmid: int, current_user: str = Depends(get_current_user)):

    vm = prox.nodes("homelab").qemu(vmid).status.current.get()

    if vm is None:
        raise HTTPException(status_code=404, detail="VM not found!")

    return vm


#start vm
@router.post('/v1/vms/{vmid}/start')
def start_vm(vmid:int, current_user: str = Depends(get_current_user), db = Depends(get_db)):
    vm = prox.nodes("homelab").qemu(vmid).status.start.post()

    log_action(db, action='start-vm', resource_type='vm', resource_id=vmid, status='success',detail=f'VM {vmid} started..')
    return vm

#stop vm
@router.post('/v1/vms/{vmid}/stop')
def stop_vm(vmid:int, current_user: str = Depends(get_current_user), db=Depends(get_db)):
    vm = prox.nodes("homelab").qemu(vmid).status.stop.post()

    log_action(db, action='stop-vm', resource_type='vm', resource_id=vmid, status='success',detail=f'VM {vmid} stopped..')
    return vm


