import smtplib
from email.mime.text import MIMEText


def send_otp_email():
    s = smtplib.SMTP('webmail.nlng.com', 25)
    msg = MIMEText("""Dear Recipient,\n\n
Kindly use the OTP below to completed your verification\n """)
    sender = 'dashboard.pms@nlng.com'
    recipients = ["ahmedrufai.otuoze@nlng.com"]
    msg['Subject'] = "OTP Verification"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    s.sendmail(sender, recipients, msg.as_string())

send_otp_email()