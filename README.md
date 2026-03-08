A complete **Cloud Native DevOps Pipeline** implementing CI/CD, GitOps, containerization, and Kubernetes deployment using modern DevOps tools.![CI Pipeline](https://github.com/dvanhu/cloud-native-devops-platform/actions/workflows/ci.yml/badge.svg)



This project demonstrates a **production-style DevOps workflow** where application code is automatically built, containerized, pushed to a registry, and deployed to Kubernetes through GitOps.

---

# Project Architecture

<img width="1536" height="1024" alt="file_000000007970720baabfba88b6fab7a8" src="https://github.com/user-attachments/assets/808dd0f9-7fb0-4c85-ab89-a95a5455bd74" />

---

# Tech Stack

| Category                | Tools Used          |
| ----------------------- | ------------------- |
| Version Control         | Git, GitHub         |
| CI Pipeline             | GitHub Actions      |
| Containerization        | Docker              |
| Container Registry      | DockerHub           |
| GitOps                  | ArgoCD              |
| Container Orchestration | Kubernetes          |
| Infrastructure          | Terraform           |

---

# Features

✔ Automated CI pipeline using GitHub Actions

✔ Docker image build and push to DockerHub

✔ Kubernetes deployment using manifests

✔ GitOps deployment with ArgoCD

✔ Automatic container image updates using ArgoCD Image Updater

✔ Scalable backend deployment (ReplicaSet)

✔ Infrastructure provisioning using Terraform

✔ Monitoring setup using Prometheus & Grafana

---

# Project Structure

```
cloud-native-devops-platform
│
├── .github
│   └── workflows
│       └── ci.yml
│
├── app
│   └── backend
│       ├── Dockerfile
│       └── application code
│
├── kubernetes
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── terraform
│   └── infrastructure configuration
│
├── monitoring
│   ├── prometheus
│   └── grafana
│
└── README.md
```

---

# CI/CD Workflow

## Continuous Integration (CI)

Triggered when code is pushed to the `main` branch.

Pipeline Steps:

1. Checkout repository
2. Login to DockerHub
3. Build Docker image
4. Tag image using Git commit SHA
5. Push image to DockerHub

Example GitHub Actions pipeline:

```
Git Push
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
Docker Push
```

---

## Continuous Deployment (CD)

Deployment is handled using **GitOps with ArgoCD**.

Workflow:

```
New Docker Image
        │
        ▼
ArgoCD Image Updater
        │
        ▼
Update Kubernetes Manifest
        │
        ▼
ArgoCD Sync
        │
        ▼
Kubernetes Deployment
```

---

# Docker Image

Docker images are pushed to DockerHub.

Repository:

```
https://hub.docker.com/r/dvanhu/devops-backend
```

Images are tagged using **Git commit SHA** for traceability.

Example:

```
dvanhu/devops-backend:ed17084659da4ab08...
```

---

# Kubernetes Deployment

The backend application is deployed using Kubernetes resources:

* Deployment
* ReplicaSet
* Service
* Ingress


# GitOps with ArgoCD

ArgoCD continuously monitors the Git repository and ensures the Kubernetes cluster matches the declared state.

Application Status:

```
Healthy
Synced
```

Deployment graph:

```
Service
   ↓
Deployment
   ↓
ReplicaSet
   ↓
Pods
```

---

# Monitoring

Monitoring stack includes:

* Prometheus (metrics collection)
* Grafana (visualization dashboards)

This enables observability of application and infrastructure metrics.
---

# Key DevOps Concepts Demonstrated

* CI/CD Automation
* Containerization
* GitOps Deployment
* Kubernetes Orchestration
* Infrastructure as Code
* Monitoring & Observability







