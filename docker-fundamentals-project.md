# Docker Fundamentals Project

## Overview
Learned Docker containers and built my own custom Docker image running a web server.

## What I Did
1. Verified Docker installation in GitHub Codespaces
2. Ran my first container (hello-world)
3. Ran an Nginx web server container with port mapping
4. Practiced core Docker commands (ps, logs, stop, start, rm, images)
5. Created a custom app with an index.html
6. Wrote a Dockerfile (FROM, COPY, EXPOSE)
7. Built a custom image (sunny-web-app)
8. Ran my own container and viewed it in the browser

## Key Concepts Learned
- Docker solves the "works on my machine" problem by packaging app + dependencies
- Dockerfile is the recipe, Image is the template, Container is the running instance
- Containers share the host OS - lightweight and fast (seconds to start)
- VMs run a full guest OS each - heavier and slower
- Port mapping (-p) connects container ports to the host

## Containers vs VMs
- VM: full guest OS, heavy (GBs), starts in minutes, strong isolation
- Container: shares host OS, light (MBs), starts in seconds, efficient

## Skills Demonstrated
- Running and managing Docker containers
- Writing Dockerfiles
- Building custom images
- Port mapping and container lifecycle

Completed: July 2026 | Part of my DevOps journey
