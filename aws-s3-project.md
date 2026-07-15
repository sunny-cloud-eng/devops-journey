# AWS S3 Static Website Project

## Overview
Hosted a live static website using only Amazon S3 - no server required - and learned S3 storage and security fundamentals.

## What I Did
1. Created an S3 bucket (globally unique name)
2. Uploaded an index.html file (an S3 object)
3. Enabled static website hosting
4. Added a bucket policy allowing public read (s3:GetObject only)
5. Accessed the live website via the S3 website endpoint
6. Emptied and deleted the bucket to clean up

## Key Concepts Learned
- S3 is unlimited, highly durable object storage (11 nines durability)
- Bucket is the container; objects are the files inside
- Bucket names are globally unique across all AWS
- Storage classes (Standard, Standard-IA, Glacier) optimize cost
- Lifecycle rules auto-move data to cheaper classes over time
- Buckets are private by default; Block Public Access prevents leaks
- Bucket policies and IAM control access; encryption protects data

## Security Insight
Misconfigured public S3 buckets are a top cause of data breaches. I keep Block Public Access on unless there is a specific need like static hosting, and grant only least-privilege access.

## Skills Demonstrated
- S3 bucket and object management
- Static website hosting
- Bucket policy configuration
- S3 security best practices
- Cost optimization awareness

Completed: July 2026 | Part of my DevOps journey
