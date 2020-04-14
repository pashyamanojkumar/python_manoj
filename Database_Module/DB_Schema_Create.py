#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","password")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create Schema as per Requirement
sql = "create database python_Class"
cursor.execute(sql)

# Fetch a single row using fetchone() method
data = cursor.fetchone()

print("SCHEMA has been created: %s" % data)

# disconnect from server
db.close()
