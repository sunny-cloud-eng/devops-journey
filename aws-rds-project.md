# AWS RDS Managed Database Project

## Overview
Launched a managed MySQL database using Amazon RDS, completing a 3-tier architecture with a secure private database tier.

## What I Did
1. Created an RDS MySQL instance (sunny-database) using Free Tier
2. Configured master username and secure password
3. Placed the database inside sunny-vpc
4. Set public access to No for security (private subnet approach)
5. Created an initial database named shopdb
6. Verified the database reached Available state and reviewed its endpoint
7. Deleted the database to avoid charges

## Key Concepts Learned
- RDS is a managed database service - AWS handles backups, patching, and failover
- Supports MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Aurora
- Automatic backups allow point-in-time recovery
- Multi-AZ keeps a standby copy in another AZ for automatic failover (disaster recovery)
- Read Replicas share read load for better performance
- Databases belong in private subnets and should not be publicly accessible

## 3-Tier Architecture Completed
Tier 1 Web: Load Balancer (public subnet)
Tier 2 App: EC2 Auto Scaling Group (private subnet)
Tier 3 Data: RDS database (private subnet)

## Multi-AZ vs Read Replicas (Interview Key)
- Multi-AZ is for high availability and disaster recovery (automatic failover)
- Read Replicas are for performance (scaling read traffic)

## Skills Demonstrated
- Managed database provisioning
- Secure database placement in a VPC
- Understanding of HA, backups, and read scaling
- 3-tier architecture design

Completed: July 2026 | Part of my DevOps journey
