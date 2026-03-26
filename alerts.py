import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    sender = r"priyadharshinivenkatesan10@gmail.com"
    receiver = r"priyadharshini.shab28@gmail.com"
    password = r"qqew lxir wbaw lxhw"   # NOT your Gmail password!

    msg = MIMEText(message)
    msg["Subject"] = "🚨 EV Battery Alert"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Alert sent successfully!")
    except Exception as e:
        print("Error sending email:", e)