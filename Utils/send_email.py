import smtplib
import os
from email.mime.text import MIMEText


def send_email(name, email, message):
    sender_email = os.getenv("SENDER_EMAIL_ADDRESS")
    sender_password = os.getenv("SENDER_EMAIL_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL_ADDRESS")

    print(sender_email, sender_password, receiver_email)

    msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg['Subject'] = "New Contact Form Message"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
