# AWS Auto Scaling Group Project

## Overview
Built an Auto Scaling Group that automatically adjusts the number of EC2 servers based on demand, with self-healing capability.

## What I Did
1. Created a Launch Template (sunny-launch-template) with a user-data startup script
2. Configured the template to auto-install Apache on each new server
3. Created an Auto Scaling Group (sunny-asg) in sunny-vpc
4. Set capacity: minimum 1, desired 2, maximum 4
5. Verified 2 servers launched automatically
6. Tested self-healing by terminating an instance and watching the ASG replace it
7. Deleted the ASG to avoid charges

## Key Concepts Learned
- Launch Template is the blueprint for each new server
- Auto Scaling Group maintains capacity between min and max
- Desired capacity is the target number of running instances
- Scaling policies add/remove servers based on metrics like CPU
- Self-healing: unhealthy instances are automatically replaced
- User data scripts configure servers automatically at launch

## Benefits
- Cost savings: pay only for needed capacity
- High availability: automatic replacement of failed instances
- Handles traffic spikes automatically

## Architecture
Load Balancer to Target Group to Auto Scaling Group of EC2 instances, all inside a VPC - a resilient, scalable design.

## Skills Demonstrated
- Launch Template configuration
- Auto Scaling Group setup
- Capacity planning (min/desired/max)
- Self-healing infrastructure
- User data automation

Completed: July 2026 | Part of my DevOps journey
