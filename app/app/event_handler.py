import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def send_alert(message, recipient_email):
    msg = MIMEText(message)
    msg["Subject"] = "Smart Surveillance Alert"
    msg["From"] = "noreply@surveillance.local"
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            # server.login("your_username", "your_password")  # optional
            server.send_message(msg)
            print(f"Alert sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

def log_event(event_type, camera_id):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {event_type} detected on camera {camera_id}")

