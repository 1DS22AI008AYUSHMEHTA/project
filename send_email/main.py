import smtplib as s
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# Set up SMTP connection
ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login(EMAIL, APP_PASSWORD)

# Email content
subject = 'Email Validation Program'
body = 'How to send a mail to multiple people using Python program'
message = f"Subject: {subject}\n\n{body}"

recipients = [
    '1ds22ai008@dsce.edu.in',
    '1ds22ai051@dsce.edu.in'
]

# Send email
ob.sendmail(EMAIL, recipients, message)
print('Mail sent successfully.')
ob.quit()
