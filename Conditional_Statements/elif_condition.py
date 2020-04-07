# elif statement
'''The elif statement allows you to check multiple expressions for
    TRUE an Execute a block of code as soon as one of the conditions
    evaluates to
Syntax:
if expression:
   statement(s)
elif expression:
   statement(s)
elif expression:
   statement(s)
else :
   statement(s)
'''
#!/usr/bin/python
fee = int(input("Enter fee:"))
if fee == 20:
    message = "if block - Condition is True"
elif fee == 10:
    message = "elif block - condition is True"
elif fee == 5:
    message = "2nd elif block - condition is True"
else:
    message = "This is Else Block and condition is False"
print(message)
