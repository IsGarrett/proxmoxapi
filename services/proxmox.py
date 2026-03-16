from proxmoxer import ProxmoxAPI
from config import settings

prox = ProxmoxAPI(
    settings.proxmox_host,
    user=settings.proxmox_user,
    token_name='proxmoxer',
    token_value=settings.proxmox_token_secret,
    verify_ssl=False
)