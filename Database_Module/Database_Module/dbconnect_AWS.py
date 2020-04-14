'''
#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("pythondb.cvjlpwf8abup.us-east-2.rds.amazonaws.com:3306","pythondb","pythondb")

# db = MySQLdb.connect("server.minnu.com","root","redhat","test_minnu")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version: %s " % data)

# disconnect from server
db.closer()

'''
import pymysql
host="pythondb.cvjlpwf8abup.us-east-2.rds.amazonaws.com"
port=3306
dbname="pythondb"
user="pythondb"
password="pythondb"
conn = pymysql.connect(host,user=user,port=port,password=password,db=dbname)