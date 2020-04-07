'''
Loops in python:
1. while :
 while expression: # True and it will execute until the false condition
    statement(s)
example:
1.
while True:
     print("Welcome to Python World")

2.
var = 1
while var <=10:
    print("I am while loop", +var, sep=":")
    var = var + 1
print("")
print("We are out side of the while loop block")

3.
passWord = ""
while passWord != 'redhat':
    passWord = input("Please enter the password: ")
    if passWord == "redhat":
        print("Correct password")
    elif passWord == 'admin@123':
        print("It was previously used password")
    elif passWord == "Redhat@123":
        print("This is your recent changed password")
    else:
        print("Incorrect password- Try again")


