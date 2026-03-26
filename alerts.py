import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    sender = ""
    receiver = ""
    password = ""

    msg = MIMEText(message)
    msg["Subject"] = "🚨 EV Battery Alert"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        print("Connecting...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        print("Logging in...")
        server.login(sender, password)

        print("Sending email...")
        server.sendmail(sender, receiver, msg.as_string())

        server.quit()
        print("✅ Alert sent!")

    except Exception as e:
        print("❌ ERROR:", str(e))
