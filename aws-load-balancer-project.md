# AWS Load Balancer (ALB) Project

## Overview
Built an Application Load Balancer distributing traffic across two EC2 web servers for high availability.

## What I Did
1. Launched two EC2 instances (sunny-web-1, sunny-web-2) in sunny-vpc
2. Installed Apache on both with different identifying pages
3. Created a Target Group (sunny-tg) with both servers
4. Created an Application Load Balancer (sunny-alb) across two AZs
5. Configured HTTP listener forwarding to the target group
6. Verified traffic distribution by refreshing the ALB DNS name
7. Deleted resources to avoid charges

## Key Concepts Learned
- Load balancers distribute traffic for availability and scalability
- ALB works at Layer 7 (HTTP/HTTPS) with URL/path routing
- NLB works at Layer 4 (TCP/UDP) for extreme performance
- Target Groups are named collections of backend servers
- Health checks auto-remove unhealthy targets and add them back on recovery
- ALB requires subnets in at least two Availability Zones

## Production Architecture
Internet to ALB (public subnet) to EC2 app servers (private subnet) to RDS database (private subnet) - the classic 3-tier design.

## Skills Demonstrated
- Application Load Balancer configuration
- Target Group and health check setup
- High availability architecture design
- Multi-AZ deployment
<img width="1298" height="462" alt="image" src="https://github.com/user-attachments/assets/11ccfe94-ec48-45bb-a143-3b173dbedf28" />

Completed: July 2026 | Part of my DevOps journey
