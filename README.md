# Automation-Emails-projects

Explanation of Two Codes
Birthay Manager :
This code reads birthday information from a CSV file and automatically sends an email to each contact.
Steps of the script:
Libraries: csv, smtplib, ssl and datetime libraries are imported.
Birthday Message: A personalized birthday message template is defined.

Email Sending:
Sender's email address and password (taken from environment variable)
SMTP connection is securely established with ssl.
Emails are sent for each contact.

Menu:
The user is given the option to add or remove names from the CSV file.
New information is requested for the addition process.
For the removal process, the name is entered and the relevant record is deleted.

Bulk E-mail:
This script sends a bulk email to a mailing list.
Steps of the Code:
Libraries: smtplib, ssl, os and datetime libraries are imported.

Email Information:
Sender's email address and password (taken from environment variable)
The email addresses of the recipients are kept in a list.
Email subject and body are defined.
Email Sending:
SMTP connection is securely established with ssl.
Email is sent to each recipient.
Date Check:
The sending date is added to the email body.
Differences:
Birthday Manager : Uses CSV file for personalized messages and automatic birthday greeting.
Bulk email: Uses a static recipient list for sending bulk emails.

Notes:
Both scripts can be added for error checking and further customization.
For security, it is important to store email passwords in environment variables or use more secure methods.
