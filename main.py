from fastapi import FastAPI
from proxmoxer import ProxmoxAPI
import os
from dotenv import load_dotenv

load_dotenv()

PROXMOX_HOST = os.getenv("PROXMOX")
PROXMOX_USER = os.getenv("PROXMOX_USER")
PROXMOX_TOKEN_SECRET = os.getenv("API_TOKEN")
PROXMOX_PORT = os.getenv("PROXMOX_PORT")


prox = ProxmoxAPI(
    PROXMOX_HOST,
    user=PROXMOX_USER,
    token_name='proxmoxer',
    token_value=PROXMOX_TOKEN_SECRET,
    verify_ssl=False
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get('/nodes')
def read_nodes():
    return prox.nodes.get()

@app.get('/node-status')
def read_status():
    return prox.nodes.status.get()

@app.get('/acl')
def read_acl():
    return prox.access.acl.get()



