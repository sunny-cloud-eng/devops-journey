# 🌩️ AWS Core Services - Quick Notes

My hands-on notes on AWS core services for interview preparation.

## 1. EC2 (Elastic Compute Cloud)
- Virtual servers in the cloud
- Pay per hour/second
- Use cases: Web servers, application backends
- Key concepts: AMI, Instance Types, Security Groups, Key Pairs

## 2. VPC (Virtual Private Cloud)
- Your own isolated network in AWS
- Contains subnets (public and private)
- Components: Route Tables, Internet Gateway, NAT Gateway
- Best practice: Multi-AZ for high availability

## 3. S3 (Simple Storage Service)
- Object storage for files, images, backups
- 99.999999999% durability (11 nines!)
- Storage classes: Standard, Infrequent Access, Glacier
- Use cases: Static websites, backups, data lakes

## 4. IAM (Identity and Access Management)
- Manage users, groups, and permissions
- Follow "Least Privilege" principle
- Components: Users, Groups, Roles, Policies
- Best practice: Use Roles for EC2, never store keys on servers

## 5. RDS (Relational Database Service)
- Managed database service (MySQL, PostgreSQL, etc.)
- Automated backups and patching
- Multi-AZ for high availability
- Read replicas for scaling reads

## 6. CloudWatch
- Monitoring and observability service
- Metrics, Logs, Alarms, Dashboards
- Integration with all AWS services
- My existing skill: I already use Site24x7 - very similar concepts!

---

## 📚 Learning Progress
- Week 1: Git & GitHub ✅
- Week 2: AWS Deep Dive (in progress)
- Week 3: Terraform (upcoming)

Last updated: July 2026