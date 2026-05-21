from celery import Celery
from config import settings


celery_app = Celery(
    'proxmox_worker',
    broker=settings.redis_url,
    backend=settings.redis_url,
    include=["workers.tasks"] 
)


celery_app.conf.beat_schedule = {
    'poll-node-metrics': {
        'task': 'workers.tasks.poll_node_metrics',
        'schedule': 60.0,
    },
    'poll-lxc-metrics': {
        'task': 'workers.tasks.poll_lxc_metrics',
        'schedule': 60.0,
    }
}

celery_app.conf.timezone = 'UTC'