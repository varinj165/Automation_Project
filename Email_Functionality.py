import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the email server and login credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email_address@gmail.com'
smtp_password = 'your_email_password'

# Set up the email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = ', '.join(sales_team_emails)
msg['Subject'] = 'Weekly Sales Report'
msg.attach(MIMEText(sales_report_html, 'html'))

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, sales_team_emails, msg.as_string())