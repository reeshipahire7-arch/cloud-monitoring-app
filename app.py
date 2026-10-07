from flask import Flask
import os
import platform
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <html>
        <head>
            <title>Cloud Monitoring Dashboard</title>
        </head>
        <body>
            <h1>Cloud Monitoring Dashboard</h1>
            <h2>Application Status: RND ✅</h2>
            <p>Hostname: {hostname}</p>
            <p>Platform: {platform.system()}</p>
            <p>Environment: AWS EC2 + Docker</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)