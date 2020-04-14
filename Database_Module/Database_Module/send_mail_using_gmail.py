#!/usr/bin/python
import smtplib

gmail_user = 'pashyamanojkumar@gmail.com'
gmail_password = 'chittu8'

from_1 = gmail_user
to = ['pashyamanojkumar@gmail.com','pashya.studunt@gmail.com']
subject = 'Sending Email using GMAIL Mail Server-Manojkumar'
body = 'Hi, \n This is a Email Test \n Thanks, \nRoot.'
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" %(from_1,", ".join(to),subject,body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.sendmail(from_1,to,email_text)
    server.close()
except:
    print('Something went wrong...')