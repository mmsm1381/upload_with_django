import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "syadtym800@gmail.com"  # Enter your address
receiver_email = "syadtym983@gmail.com"  # Enter receiver address
password = "37500879m"
message = """\
Subject: Hi there

some body push on ur repo ."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
