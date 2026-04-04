# Cloud Native DevOps Platform

![CI Pipeline](https://github.com/dvanhu/cloud-native-devops-platform/actions/workflows/ci.yml/badge.svg)

A **production-style Cloud Native DevOps platform** demonstrating end-to-end CI/CD and GitOps using GitHub Actions, Docker, ArgoCD, and Kubernetes — with infrastructure provisioning via Terraform and observability via Prometheus & Grafana.

> Code is automatically built, containerized, pushed to DockerHub, and deployed to Kubernetes through GitOps — no manual steps.

---

## Architecture Overview

```
Developer pushes code
        │
        ▼
  GitHub Actions (CI)
        │
   ┌────┴────┐
   │  Docker │  Build → Tag (Git SHA) → Push to DockerHub
   └────┬────┘
        │
        ▼
ArgoCD Image Updater
        │   Detects new image tag, updates K8s manifest
        ▼
   ArgoCD Sync
        │   Reconciles cluster state with Git
        ▼
Kubernetes Cluster
  ┌─────────────────────────────────┐
  │  Ingress → Service → Deployment │
  │           └── ReplicaSet        │
  │                └── Pods         │
  └─────────────────────────────────┘
        │
        ▼
  Prometheus + Grafana (Monitoring)
```

---

## Tech Stack

| Category | Tool |
|---|---|
| Version Control | Git, GitHub |
| CI Pipeline | GitHub Actions |
| Containerization | Docker |
| Container Registry | DockerHub |
| GitOps | ArgoCD + ArgoCD Image Updater |
| Orchestration | Kubernetes |
| Infrastructure as Code | Terraform (HCL) |
| Monitoring & Observability | Prometheus, Grafana |
| Application | Python (backend) |

**Language breakdown:** Python 40% · HCL (Terraform) 31% · Dockerfile 29%

---

## Project Structure

```
cloud-native-devops-platform/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── app/
│   └── backend/
│       ├── Dockerfile          # Container image definition
│       └── ...                 # Python application code
├── kubernetes/
│   ├── deployment.yaml         # App deployment & ReplicaSet
│   ├── service.yaml            # ClusterIP / LoadBalancer
│   └── ingress.yaml            # Ingress routing rules
├── gitops/                     # ArgoCD application manifests
├── terraform/                  # Infrastructure provisioning
├── monitoring/
│   ├── prometheus/             # Scrape configs & rules
│   └── grafana/                # Dashboard definitions
├── docs/                       # Additional documentation
├── docker-compose.yml          # Local development setup
└── README.md
```

---

## Getting Started

### Prerequisites

- Docker & Docker Compose
- `kubectl` configured against a Kubernetes cluster
- Terraform ≥ 1.0
- ArgoCD installed on your cluster
- DockerHub account

### 1. Local Development

```bash
git clone https://github.com/dvanhu/cloud-native-devops-platform.git
cd cloud-native-devops-platform
docker-compose up --build
```

### 2. Provision Infrastructure (Terraform)

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

### 3. Deploy to Kubernetes (Manual)

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml
```

### 4. Set Up ArgoCD

```bash
# Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Apply the GitOps app definition
kubectl apply -f gitops/
```

ArgoCD will then continuously sync the cluster state with this repository.

---

## CI/CD Pipeline

### Continuous Integration — GitHub Actions (`.github/workflows/ci.yml`)

Triggered on every push to `main`:

```
1. Checkout repository
2. Login to DockerHub
3. Build Docker image
4. Tag image with Git commit SHA
5. Push image to DockerHub → dvanhu/devops-backend:<commit-sha>
```

### Continuous Deployment — GitOps with ArgoCD

```
New image pushed to DockerHub
          │
          ▼
ArgoCD Image Updater detects new tag
          │
          ▼
Auto-updates Kubernetes manifest in Git
          │
          ▼
ArgoCD syncs cluster → rolling update
```

Images are tagged by Git commit SHA for full traceability:
```
dvanhu/devops-backend:ed17084659da4ab08...
```

DockerHub repository: [hub.docker.com/r/dvanhu/devops-backend](https://hub.docker.com/r/dvanhu/devops-backend)

---

## Kubernetes Resources

| Resource | Purpose |
|---|---|
| `Deployment` | Manages pod lifecycle and rolling updates |
| `ReplicaSet` | Ensures desired number of pod replicas |
| `Service` | Exposes the application within the cluster |
| `Ingress` | Routes external HTTP traffic to the service |

---

## Monitoring

Prometheus scrapes application and cluster metrics; Grafana provides dashboards for:

- Pod health and restart counts
- Resource utilization (CPU, memory)
- Request rates and latency
- Deployment rollout status

---

## Required Secrets (GitHub Actions)

Set these in your repository's **Settings → Secrets and Variables → Actions**:

| Secret | Description |
|---|---|
| `DOCKERHUB_USERNAME` | Your DockerHub username |
| `DOCKERHUB_TOKEN` | DockerHub access token |

---

## Key DevOps Concepts Demonstrated

- **CI/CD Automation** — Zero-touch pipeline from commit to deployment
- **GitOps** — Git as the single source of truth for cluster state
- **Containerization** — Immutable, reproducible Docker images
- **Kubernetes Orchestration** — Scalable, self-healing deployments
- **Infrastructure as Code** — Reproducible infra via Terraform
- **Monitoring & Observability** — Metrics, dashboards, and alerting
- **Image Traceability** — SHA-tagged images for audit and rollback
