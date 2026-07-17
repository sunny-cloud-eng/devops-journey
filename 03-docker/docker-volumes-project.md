# Docker Volumes Project

## Overview
Learned how Docker Volumes provide persistent storage that survives container deletion, and proved it hands-on.

## What I Did
1. Created a named volume (sunny-data)
2. Ran a container with the volume attached to /data
3. Wrote a file inside the volume from within the container
4. Deleted the container completely
5. Created a NEW container using the same volume
6. Verified the data was still there - it survived!
7. Cleaned up the container and volume

## Key Concepts Learned
- Container storage is ephemeral - data is lost when a container is deleted
- Volumes store data OUTSIDE the container, so it persists
- Named Volumes are managed by Docker (best for databases and app data)
- Bind Mounts map a specific host folder into the container (best for development)
- In Docker Compose, volumes keep database data safe across docker compose down

## Analogy
A container is like a hotel room (temporary); a volume is like your suitcase (data travels safely with you).

## Key Commands
- docker volume create sunny-data
- docker volume ls
- docker run -d -v sunny-data:/data --name vol-test nginx
- docker exec -it vol-test sh
- docker volume rm sunny-data

## Skills Demonstrated
- Persistent storage with Docker volumes
- Named volumes vs bind mounts
- Data persistence across container lifecycle
- Volume usage in Docker Compose

<img width="975" height="493" alt="image" src="https://github.com/user-attachments/assets/97169b8a-6a51-4cef-932d-67e1de4f0058" />


Completed: July 2026 | Part of my DevOps journey
