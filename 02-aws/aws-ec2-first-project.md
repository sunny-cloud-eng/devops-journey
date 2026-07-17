# Project: My First EC2 Web Server on AWS

## Overview
Launched and configured an EC2 instance on AWS, deployed a live Apache web server, and troubleshot a real network access issue.

## What I Did
1. Created a secure IAM user (not root) following best practices
2. Set up billing alerts to control costs
3. Launched a t2.micro EC2 instance (Free Tier eligible)
4. Connected via EC2 Instance Connect
5. Installed and configured Apache (httpd) web server
6. Hosted a static HTML page
7. Troubleshot a Security Group issue (added HTTP port 80 inbound rule)
8. Verified the live website via public IP
9. Terminated resources to avoid charges

## Challenge I Solved
The website was not loading initially. I diagnosed the issue to the Security Group - the inbound rule for HTTP port 80 was missing. After adding the rule allowing HTTP traffic from anywhere, the site loaded successfully.

## Services Used
- EC2 (Elastic Compute Cloud)
- IAM (Identity and Access Management)
- Security Groups (virtual firewall)
- AWS Billing and Budgets

## Key Learnings
- Security Groups act as virtual firewalls controlling inbound and outbound traffic
- A running server is unreachable if the required port is not open
- Always use IAM users, never root for daily tasks
- Free Tier eligibility matters for cost control
- Always terminate resources when done

## Skills Demonstrated
- Cloud infrastructure provisioning
- Linux server administration
- Web server configuration (Apache)
- Network troubleshooting (Security Groups)
- Cost management and security best practices

Completed: July 2026 | Part of my DevOps journey
