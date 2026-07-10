# EC2 in Custom VPC + Security Groups Project

## Overview
Launched an EC2 web server inside a custom-built VPC and configured Security Groups following least-privilege best practices.

## What I Did
1. Launched EC2 (t2.micro) inside sunny-vpc public subnet
2. Enabled auto-assign public IP
3. Created Security Group sunny-web-sg with least-privilege rules
4. Restricted SSH (port 22) to My IP only
5. Allowed HTTP (port 80) from anywhere
6. Installed and configured Apache web server
7. Verified live website running inside custom VPC
8. Terminated instance to avoid charges

## Security Groups vs NACLs (Key Learning)
- Security Group: instance-level, stateful, allow-only rules
- NACL: subnet-level, stateless, allow and deny rules
- Used SG as primary control with least-privilege source restrictions

## Bastion Host Concept
For private subnet access, a bastion host in the public subnet acts as a secure jump server. Modern alternative: AWS Systems Manager Session Manager.

## Skills Demonstrated
- EC2 deployment in custom VPC
- Security Group configuration
- Least-privilege network security
- Understanding of SG vs NACL
- Bastion host architecture

Completed: July 2026 | Part of my DevOps journey
