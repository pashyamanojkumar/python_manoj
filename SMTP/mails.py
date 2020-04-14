import smtplib
sender = "pashyamanojkumar@gmail.com"
receivers = "pashya.student@igu.edu"
message = """
From: pmr <pashyamanojkumar@gmail.com>
To: pashya.student@igu.edu
MIME-Version:1.0
Content-type: text/html
Subject: Email Test

<b>This is Test mail</b>
<h1>This is Headline</h1>
"""
try:
    smtpObject = smtplib.SMTP('smtp.gmail.com',587)
    smtpObject.sendmail(sender,receivers,message)
    print("Email has been sent Successfully!")
except Exception as e:
    print("Due to {e} mail was not delivered!")