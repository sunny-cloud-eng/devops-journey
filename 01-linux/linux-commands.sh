#!/bin/bash

# ==============================================
# Linux Commands Reference - Sunny's Cheat Sheet
# ==============================================

echo "=========================================="
echo "System Health Check Script"
echo "=========================================="

# Check current directory
echo "Current Directory:"
pwd

# List files
echo ""
echo "Files in current directory:"
ls -la

# Check disk space
echo ""
echo "Disk Space:"
df -h

# Check memory usage
echo ""
echo "Memory Usage:"
free -h

# Check running processes (top 5)
echo ""
echo "Top 5 Processes:"
ps aux --sort=-%cpu | head -6

echo ""
echo "=========================================="
echo "Health check complete!"
echo "=========================================="