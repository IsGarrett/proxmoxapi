

def parse_lxc_status(raw: dict) -> dict:
    return {
        "vmid": raw.get("vmid"),
        "name": raw.get("name"),
        "status": raw.get("status"),
        "cpu": raw.get("cpu"),
        "memory": raw.get("mem"),
    }

def parse_node_response(raw: dict) -> dict:
    return {
        'uptime': raw.get('uptime'),
        'node': raw.get('node'),
        'maxcpu': raw.get('maxcpu'),
        'status': raw.get('status'),
        'cpu': raw.get('cpu'),
        'disk': raw.get('disk'),
        
    }
   