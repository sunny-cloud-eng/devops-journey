# AWS VPC Design Project

## Overview
Designed and built a custom AWS VPC from scratch with public and private subnets, following production-grade network architecture.

## Architecture Built
- VPC: sunny-vpc (CIDR 10.0.0.0/16)
- Public Subnet: 10.0.1.0/24 in AZ ap-south-1a
- Private Subnet: 10.0.2.0/24 in AZ ap-south-1b
- Internet Gateway: sunny-igw attached to VPC
- Public Route Table: routes 0.0.0.0/0 to Internet Gateway
- Private Route Table: no internet route (isolated)

## Key Concepts Learned
- CIDR notation: smaller prefix means bigger network (/16 vs /24)
- A subnet is public only if its route table routes to an Internet Gateway
- Private subnets stay isolated for databases and backend servers
- NAT Gateway allows private subnets outbound internet access while blocking inbound
- Multi-AZ subnet placement provides high availability

## Real-World Application
This is the foundation of a 3-tier architecture: Load Balancer in public subnet, application servers and databases in private subnets.

## Skills Demonstrated
- VPC and subnet design
- CIDR planning
- Route table configuration
- Internet Gateway setup
- Network security architecture

Completed: July 2026 | Part of my DevOps journey
