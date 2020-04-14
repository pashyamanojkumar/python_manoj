#!/usr/bin/python

import smtplib

TO = 'pashyamanojkumar.com'
SUBJECT = 'Send email using SMTPLIB in Python'
TEXT = 'Here is the message we would like to send'

# Gmail Credentials
gmail_sender='pashyamanojkumar@gmail.com'
gmail_password='Chittu@88'

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gmail_sender,gmail_password)

BODY='\r\n'.join([
    'To: %s' % TO,
    'From: %s' % gmail_sender,
    'Subject: %s' % SUBJECT,
    '',
    TEXT
    ])
try:
    server.sendmail(gmail_sender,[TO],BODY)
    print('email sent')
except:
    print('error sending email')

server.quit()