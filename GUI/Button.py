# Importing Modules and Classes from a Module
from tkinter import  *
from tkinter import messagebox

# Creating a Variable
top = Tk()
top.geometry("500x500")

# Create a Function
def helloCallBack():
    msg = messagebox.showinfo("HOME","Welcome to Python GUI World")

B = Button(top,text="CLICK TO LOGIN",command=helloCallBack)
B.place(x=50,y=10)

top.mainloop()
# print(top,id(top),type(top))
-----------------------------------------------------
Launch a Website/WebApplication using Python
Client side coding/programming: HTML, CSS & JS
Server side coding/programming: Python

AWS Cloud:
    - Windows -IIS Webserver
    - Linux
Operating system : Linux
    - WebServer -Apache Httpd
    - Download, Install & Configure apache http server on Linux
        - Redhat/CentOS/AmazonLinux:
           # yum install http* ~y
           # systemctl status httpd.service
           # systemctl enable httpd.service
           # systemctl start httpd.service
           # systemctl status httpd.service

           # cd/var/www/html

           # ls -lrt

           html/
           cgi-bin/

Client side coding/programming: HTML, CSS & JS
# cd html/
Example: index.html
<html>
<body>
<h1>Welcome to Python WOrld</h1>
</body>
</html>

Server side coding/programming: Python
# cd cgi-bin/
Example: checkbox.py
import cgi