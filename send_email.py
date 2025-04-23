# Program: Plant Moisture Sensor with Email Notification
# Author: Xuanru Guo
# Student Number: W20109677
# Date: 21/4/2025
# Description: create email test script
# Course & Year: Project Semester 3

import smtplib
from email.message import EmailMessage

# Set the sender email and password and recipient email
from_email_addr = "1241428411@qq.com"
from_email_pass = "qpxzanjnrhwejejh"
to_email_addr = "2722458837@qq.com"

# Create a message object
msg = EmailMessage()

# Set the email body
body = "Hello from Raspberry Pi"
msg.set_content(body)

# Set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# Set your email subject
msg['Subject'] = 'TEST EMAIL'

# Connecting to server and sending email
# Provider's SMTP server details
server = smtplib.SMTP('smtp.qq.com', 587)

# Use TLS
server.starttls()

# Login to the SMTP server
server.login(from_email_addr, from_email_pass)

# Send the message
server.send_message(msg)
print('Email sent')

# Disconnect from the server
server.quit()
