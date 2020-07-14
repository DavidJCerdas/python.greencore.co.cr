#!/usr/bin/python3
"""
    Just a routine practice: Getting familiar with sending emails using Python3.
"""
import smtplib
import getpass
import sys

script_name = sys.argv[0]
smtp_server = 'smtp.gmail.com'
port = 587
from_addr = 'xxxx@gmail.com'
to_addrs = input('Please put the destination email:\n')
subject = f'Test email from {from_addr} using {script_name}'
msg_body = input('Put here the body of the message:\n')
email_content = 'Subject:' + subject + '\n' + msg_body
# In case of a gmail account, the password is taken from https://myaccount.google.com/apppasswords
password = getpass.getpass(f'Please provide the password for {from_addr}:\n')

# Opening secure SMTP Connection to the port on the smtp_server
try:
    smtp_object = smtplib.SMTP(smtp_server, port)
    smtp_object.starttls()
    smtp_object.ehlo()
except Exception as e:
    print(f"Something went wrong with the connection: {e}")
    smtp_object.quit()

print(f"loging into the account: {from_addr}")
try:
    smtp_object.login(from_addr, password)
except Exception as e:
    print(f"Something went wrong with the login to the email {from_addr}: {e}")
    smtp_object.quit()    

print(f"Sending the email...")
try:
    smtp_object.sendmail(from_addr, to_addrs, email_content)
    smtp_object.quit()
except Exception as e:
    print(f"Something went wrong sending the email:{e}")
