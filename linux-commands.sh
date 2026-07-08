#!/b**/bash

# ========================**====================
# Linux Comm**ds Reference - Sunny's Cheat Shee**# ===============================**=============

echo "============**============================"
ech**"System Health Check Script"
echo**=================================**======="

# Check current directo**
echo "Current Directory:"
pwd

#**ist files
echo ""
echo "Files in **rrent directory:"
ls -la

# Check**isk space
echo ""
echo "Disk Spac**"
df -h

# Check memory usage
ech**""
echo "Memory Usage:"
free -h

**Check running processes (top 5)
e**o ""
echo "Top 5 Processes:"
ps a** --sort=-%cpu | head -6

echo ""
**ho "=============================**==========="
echo "Health check c**plete!"
echo "===================**====================="