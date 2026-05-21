from workers.celery_app import celery_app
from services.proxmox import prox
from models.node_metric import NodeMetric
from models.lxc_metric import LxcMetric
from db import SessionLocal


@celery_app.task
def poll_node_metrics():
    db = SessionLocal()

    try:
        nodes = prox.nodes.get()
        for node in nodes:
            metric = NodeMetric(
                node  = node.get('node'),
                cpu = node.get('cpu'),
                memory = node.get('mem'),
                max_memory = node.get('maxmem'),
                disk=node.get("disk"),
                max_disk=node.get("maxdisk"),
                uptime=node.get("uptime"),
                status=node.get("status")
            )
            db.add(metric)
        db.commit()
    finally:
        db.close()
    
@celery_app.task
def poll_lxc_metrics():
    db = SessionLocal()

    try:
        containers = prox.nodes("homelab").lxc.get()
        for container in containers:
            metric = LxcMetric(
                vmid = container.get('vmid'),
                name = container.get('name'),
                status = container.get('status'),
                cpu = container.get('cpu'),
                memory = container.get('mem')
            )
            db.add(metric)
        db.commit()
    finally:
        db.close()





