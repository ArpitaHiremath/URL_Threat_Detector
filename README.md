# URL_Threat_Detector

# 🔒 Website Threat Detection Using Nmap and Flask

## 📘 Project Description

This project is a **real-time website threat detection system** built using **Flask** and **Nmap**. The web application allows users to input a website URL, automatically resolves it to an IP address, performs a security scan using Nmap, displays the scan result on the web page, stores the logs in a JSON file, and sends an email alert containing the scan details.

It's designed to help developers and cybersecurity enthusiasts quickly analyze websites for open ports and potential vulnerabilities, with a simple and user-friendly interface.

---

## 🚀 Features

- 🌐 Input a URL and scan its resolved IP using Nmap.
- 🧾 View real-time scan results on the website.
- 📁 Automatically log all scans to `logs.json`.
- 📬 Send scan results via email using Gmail SMTP.
- 🕒 View history of past scan logs on a separate page.

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Nmap
- HTML + Jinja Templates
- Gmail SMTP (for alerts)
- JSON for log storage

---

## 📂 Project Structure

project/
├── app.py # Main Flask application
├── logs.json # Stores past scan logs
├── templates/
│ ├── index.html # Homepage template
│ └── logs.html # Logs viewing page



---

## ⚙️ Setup Instructions

1. **Install required packages:**
   ```bash
   pip install flask
   sudo apt install nmap

2. **Configure Gmail for Alerts:**
   
    Enable 2FA on your Gmail.

    Generate an App Password.

    Replace in app.py
    ```bash
    
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"

3. Run the app:
   ```bash
   python app.py
4. Visit:
    open http://  link in your browers.

🔐 Security Notice

Do NOT share or hardcode real email passwords in public repositories. Use environment variables or config files in production.
