import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

# SMTP server details
smtp_server = 'XXXXXXXX'
smtp_port = "XXX"  # SSL port
smtp_user = 'XXXXXXXXX'  # The user account for the SMTP
smtp_password = 'XXXXXXX'  # The password for the SMTP account

# Email content
subject = 'Investment Proposal From PLAP - Crypto Coin for sports & Fitness'

# HTML body
html_body = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Opportunity Email</title>
</head>
<body>
    <p>Hi {name},</p>
    <p>Thank you for your time!</p>
    <p>Best regards,<br>
    <strong>Ahmed Y.</strong><br>
    Founder & CEO<br>
    PlayApp AIO Inc.<br>
    Ontario, Canada</p>
     <p>If you wish to unsubscribe from future investment email proposals, <a href="https://playappeconomy.com/#">click here</a>.</p>
</body>
</html>
'''

# Track email status
successful_sends = 0
failed_sends = 0
valid_emails = []

# Open CSV file with email and name data
with open('demo.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['firstname'] 
        to_email =row['emails']
        companies = row['companies']

        # Personalize email body
        body = html_body.format(name=name,companies=companies)

        # Create the email
        msg = MIMEMultipart('alternative')
        msg['From'] = "XXXXX" #'Ahmed Yasin <founder@playappeconomy.com>'
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))  # Changed to 'html' for formatting

        # Send the email
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(smtp_user, smtp_password)
                server.sendmail(msg['From'], to_email, msg.as_string())
                successful_sends += 1
                valid_emails.append(row)  # Save valid email info
                print(f"Email sent successfully to {to_email}")
        except smtplib.SMTPRecipientsRefused as e:
            failed_sends += 1
            print(f"Failed to send email to {to_email}. Error: {e}")
        except Exception as e:
            failed_sends += 1
            print(f"Failed to send email to {to_email}. Error: {e}")

# Print summary
print(f"Total successful emails: {successful_sends}")
print(f"Total failed emails: {failed_sends}")