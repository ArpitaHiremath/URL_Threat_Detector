from flask import Flask, request, render_template
import socket
import subprocess
import datetime
import json
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
LOG_FILE = "logs.json"

# Load logs from JSON
def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

# Save logs to JSON
def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

# Send email alert
def send_email(subject, message, to_email):
    try:
        sender_email = "cstest12224@gmail.com"  # 👈 Replace with your email
        sender_password = "nnxc tncl bzan skha"  # 👈 Replace with your Gmail App Password

        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print("✅ Email sent!")
        return True
    except Exception as e:
        print(f"❌ Email error: {e}")
        return False

# Main UI
@app.route("/", methods=["GET", "POST"])
def index():
    scan_result = None
    if request.method == "POST":
        url = request.form["url"]
        try:
            ip = socket.gethostbyname(url)
            timestamp = str(datetime.datetime.now())

            output = subprocess.check_output(["nmap", "-Pn", ip]).decode()

            log_entry = {
                "url": url,
                "ip": ip,
                "timestamp": timestamp,
                "result": output
            }

            logs = load_logs()
            logs.insert(0, log_entry)
            save_logs(logs)

            # Send email alert
            send_email(
                subject=f"Nmap Scan Report: {url}",
                message=f"Scan on {url} ({ip}) at {timestamp}\n\n{output}",
                to_email="arpitahiremath443@gmail.com"  # 👈 Replace with recipient's email
            )

            scan_result = output
        except Exception as e:
            scan_result = f"Error: {str(e)}"

    return render_template("index.html", result=scan_result)

# View past scan logs
@app.route("/logs")
def view_logs():
    logs = load_logs()
    return render_template("logs.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
