from flask import Flask, render_template_string
import requests
import time

app = Flask(__name__)

# The websites we want to monitor
SITES_TO_MONITOR = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org",
]

def check_site(url):
    """Check if a site is up and measure response time."""
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        elapsed = round((time.time() - start) * 1000)  # milliseconds
        if response.status_code == 200:
            return {"url": url, "status": "UP", "code": response.status_code, "time_ms": elapsed}
        else:
            return {"url": url, "status": "DOWN", "code": response.status_code, "time_ms": elapsed}
    except Exception:
        return {"url": url, "status": "DOWN", "code": "N/A", "time_ms": "N/A"}

DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <title>UptimeGuard - by Sunny</title>
    <meta http-equiv="refresh" content="30">
    <style>
        body { font-family: Arial; background: #1a1a2e; color: #eee; padding: 40px; }
        h1 { color: #4ecca3; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #444; }
        th { background: #16213e; color: #4ecca3; }
        .up { color: #4ecca3; font-weight: bold; }
        .down { color: #e94560; font-weight: bold; }
        .footer { margin-top: 30px; color: #888; font-size: 14px; }
    </style>
</head>
<body>
    <h1>UptimeGuard Monitoring Dashboard</h1>
    <p>Real-time status of monitored services (auto-refreshes every 30s)</p>
    <table>
        <tr><th>Service</th><th>Status</th><th>HTTP Code</th><th>Response Time</th></tr>
        {% for site in results %}
        <tr>
            <td>{{ site.url }}</td>
            <td class="{{ 'up' if site.status == 'UP' else 'down' }}">{{ site.status }}</td>
            <td>{{ site.code }}</td>
            <td>{{ site.time_ms }} ms</td>
        </tr>
        {% endfor %}
    </table>
    <p class="footer">UptimeGuard | Built by Sunny | Future NZ DevOps Engineer</p>
</body>
</html>
"""

@app.route('/')
def dashboard():
    results = [check_site(url) for url in SITES_TO_MONITOR]
    return render_template_string(DASHBOARD, results=results)

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

@app.route('/api/status')
def api_status():
    """JSON API endpoint - useful for automation and other tools."""
    results = [check_site(url) for url in SITES_TO_MONITOR]
    return {"services": results}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
