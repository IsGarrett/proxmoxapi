from workers.celery_app import celery_app
from services.proxmox import prox
from models.node_metric import NodeMetric
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

