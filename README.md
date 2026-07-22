# ProxPrism

ProxPrism is a self-hosted REST API that gives you visibility into your Proxmox homelab infrastructure. It's built on FastAPI and exposes endpoints to provision, manage, and monitor your VMs and LXC containers directly from one single API.

A Celery and Redis pipeline continuously polls your Proxmox cluster in the background, persisting node and container metrics to PostgreSQL for historical analysis. A Grafana dashboard surfaces both live API metrics (via Prometheus) and historical infrastructure data from the database.

JWT authentication protects all endpoints, and the full stack deploys via Docker Compose.


## Tech Stack

- **FastAPI** — REST API framework
- **PostgreSQL** — relational database for historical metrics and user storage
- **SQLAlchemy** — ORM and database migrations via Alembic
- **Celery** — distributed task queue for background metric polling
- **Redis** — message broker for Celery
- **Proxmoxer** — Python client for the Proxmox REST API
- **Prometheus** — metrics scraping and storage
- **Grafana** — observability dashboards
- **Docker Compose** — local development and deployment
- **JWT** — API authentication via python-jose and passlib

## API Work-flow

A tool/developer sends an HTTP request
FastAPI receives it
Checks the JWT token is valid
Calls the ProxMox via proxmoxer
Returns the data as JSON
 
## Background Collection
Celery Beat deploys every 60 seconds
It puts a job on the Redis queue
Celery Worker picks the job up
Calls the Proxmox via proxmoxer
Writes the metrics to PostgreSQL

## Observability
Grafana reads from Prometheus (API Metrics)
Grafana reads from PostGreSQL (infrastructure history)
Dashboard shows everything in one place. 



## Prerequisites 

Docker Desktop
Proxmox Server with an API token created
Git to clone the repo


## Quick Start
1) Clone the repo <git clone <repo-url>>
2) Copy the .env example to .env and fill in your values
3) Run docker-compose up --build

The API will be available at `http://localhost:8000`
FastAPI's interactive docs are availble at `http://localhost:8000/docs`






## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/auth/register` | Register a new user |
| POST | `/v1/auth/login` | Login and receive a JWT token |

### Audit Logs
| Method | Endpoint | Description |
| GET | `/v1/audit` | Returns Audit Log table |
| GET | `/v1/audit/{resource_type}` | Returns Audit Log table filtered by resource type|


### Nodes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/nodes` | List all Proxmox nodes and current stats |
| GET | `/v1/nodes/{node}/metrics` | Historical metrics for a specific node |

### Virtual Machines
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/vms` | List all VMs |
| GET | `/v1/vms/{vmid}` | Get details for a specific VM |
| POST | `/v1/vms` | Provision a new VM |
| DELETE | `/v1/vms/{vmid}` | Destroy a VM |
| POST | `/v1/vms/{vmid}/start` | Start a VM |
| POST | `/v1/vms/{vmid}/stop` | Stop a VM |

### Containers
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/containers` | List all LXC containers |
| GET | `/v1/containers/{vmid}` | Get details for a specific container |
| POST | `/v1/containers` | Create a new container |
| DELETE | `/v1/containers/{vmid}` | Destroy a container |
| POST | `/v1/containers/{vmid}/start` | Start a container |
| POST | `/v1/containers/{vmid}/stop` | Stop a container |

### Health
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | API health check |
| GET | `/health/db` | Database connectivity check |
| GET | `/health/nodes` | Proxmox connectivity check |




![alt text](<Screenshot 2026-07-06 at 3.12.41 PM.png>)


![alt text](<Screenshot 2026-07-06 at 3.13.07 PM.png>)