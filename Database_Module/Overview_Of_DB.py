# Store Data Part of Database
# Humans are communicating with the help of language i.e. English
RDBMS:
Language : ANSII SQL
 All the wendors they have separate DB
1. GadFly
2. mSQL
3. MySQL
4. PostgreSQL
5. Microsoft SQL Server 2000
6. Informix
7. Interbase
8. Oracle
9. Sybase
10. mariadb

1. Importing the API module.
2. Acquiring a connection with the database.
3. Issuing SQL statements and stored procedures.
4. Closing the connection.

pip search oracle
pip download oracle
pip install oracle

--Following is a simple diagram showing SQL Architecture:
|
|
Query Language <-- Parser + Optimizer
|
|
DBMS Engine <-- File Manager + Transaction Manager
|
|
Physical Database

SQL Commands:
DDL, DML, DQL, DCL & TCL in SQL

import  MySQLdb
db = MySQLdb.connect("hostname/ip:port","username","password","Schema")
cursor = db.cursor()
cursor.execute("select * from emp where empname like '%pashya%'")
data = cursor.fetchone()
print(f"Please find the Employee Details: {data}")
db.close()
