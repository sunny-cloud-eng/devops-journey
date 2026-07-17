# Docker Compose Multi-Container Project

## Overview
Used Docker Compose to run a web server (nginx) and a database (MySQL) together with a single command.

## What I Did
1. Created a docker-compose.yml defining two services (web and database)
2. Configured nginx with port mapping 8080:80
3. Configured MySQL with environment variables (root password and database name)
4. Started both containers with one command: docker compose up -d
5. Verified both running with docker compose ps
6. Viewed the live Nginx page in the browser
7. Cleaned up with docker compose down

## Key Concepts Learned
- Docker Compose defines multiple containers (services) in one YAML file
- One command starts all: docker compose up; one stops all: docker compose down
- Compose creates a shared network automatically
- Services communicate using their service names as hostnames
- YAML uses spaces (not tabs) with consistent 2-space indentation

## Challenge Solved
Fixed a YAML parsing error (mapping key image already defined) caused by incorrect indentation, by recreating the file with clean, consistent spacing.

## Skills Demonstrated
- Writing docker-compose.yml files
- Multi-container orchestration
- Service networking and environment configuration
- YAML troubleshooting

Completed: July 2026 | Part of my DevOps journey
