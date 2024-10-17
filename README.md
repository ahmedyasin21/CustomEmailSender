# ### README: Email Sending Script Using SMTP with CSV Data

#### Overview
This Python script sends personalized investment proposal emails using an SMTP server. It reads recipient data from a CSV file and sends HTML emails to a list of email addresses using the SMTP protocol.

#### Prerequisites
To run this script, ensure you have the following:

1. Python 3.x installed on your system.
2. Required libraries: `smtplib`, `email`, and `csv` (built-in).
3. Access to an SMTP server (such as Gmail, SMTP2GO, etc.).
4. A CSV file containing recipient information (name, email, and company details).

#### Installation

No external libraries are required as all dependencies are built into Python. Make sure you have the correct version of Python installed.

#### Configuration

Before running the script, configure the following parameters:

1. **SMTP server details**: Replace the placeholders with your SMTP server credentials:
   ```python
   smtp_server = 'XXXXXXXX'
   smtp_port = 'XXX'  # Example: '587'
   smtp_user = 'XXXXXXXXX'
   smtp_password = 'XXXXXXX'
   ```

2. **Email Content**: Customize the subject and HTML body of the email:
   ```python
   subject = 'Investment Proposal From PLAP - Crypto Coin for sports & Fitness'

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
   ```

3. **CSV File Format**: Your CSV file should contain the following columns:
   - `firstname` (Name of the recipient)
   - `emails` (Recipient’s email address)
   - `companies` (Company name, if applicable)

#### CSV File Example
Your CSV file (`demo.csv`) should be structured like this:

| firstname | emails                | companies        |
|-----------|-----------------------|------------------|
| John      | john.doe@example.com   | ABC Corp         |
| Jane      | jane.smith@example.com | XYZ Inc.         |

#### Running the Script
1. Ensure your SMTP server credentials are correct.
2. Place your CSV file (e.g., `demo.csv`) in the same directory as the script.
3. Run the script in the terminal or your preferred Python IDE:
   ```bash
   python email_sender.py
   ```

#### Email Status
The script will print the status of each email sent:
- Successful sends will print a message like: `Email sent successfully to john.doe@example.com`
- Failed attempts will display the specific error message.

#### Summary Output
After all emails are processed, the script prints a summary:
```bash
Total successful emails: X
Total failed emails: Y
```

#### Notes
- **SMTP Configuration**: If you're using a service like Gmail, ensure you have enabled "Less Secure Apps" or have an App Password configured for SMTP access.
- **TLS/SSL**: The script uses SMTP with the specified port for SSL/TLS. Update the `smtp_port` based on your SMTP provider’s requirements.
  
#### License
This project is open-source and free to use.

#### Support
For questions or issues, please contact: ahmedyasin1947@gmail.com
