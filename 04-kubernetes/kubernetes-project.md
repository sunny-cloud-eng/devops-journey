# Kubernetes Fundamentals Project

## Overview
Set up a Kubernetes cluster using kind in Codespaces and deployed a self-healing, scalable nginx application using YAML manifests.

## What I Did
1. Installed kubectl and kind in Codespaces
2. Created a Kubernetes cluster (sunny-cluster)
3. Wrote a Deployment manifest (3 replicas of nginx)
4. Applied it with kubectl apply
5. Verified 3 Pods running
6. Tested self-healing by deleting a Pod and watching it auto-replace
7. Created a Service manifest for stable networking
8. Managed everything using declarative YAML files

## Key Concepts Learned
- Pod: smallest unit, wraps a container
- Deployment: manages Pods, ensures desired replicas, self-healing
- Service: stable address and load balancing for Pods
- kubectl: the command tool to control Kubernetes
- Declarative YAML manifests define desired state

## Kubernetes vs Earlier Concepts
- Pod is like a container (Docker)
- Deployment is like an Auto Scaling Group (self-healing)
- Service is like a Load Balancer (stable address + load balancing)

## Skills Demonstrated
- Kubernetes cluster setup (kind)
- Writing Deployment and Service manifests
- kubectl operations
- Self-healing and scaling
- Declarative infrastructure with YAML

<img width="975" height="497" alt="image" src="https://github.com/user-attachments/assets/a86d777b-1b1c-439b-bd59-a960f5dcb127" />


Completed: July 2026 | Part of my DevOps journey
