'''
What is Exception:
An exception is an event, which occurs during the execution of a program that
     disrupts the normal flow of the programs instructions.

In general, when a python script encounters a situation that it cannot
      cope with, it raises an exception.

An exception is a python object that represents an error.
'''
'''name ="Manoj"
value = 8
sum =name + value
print(sum)
'''
'''
# Declaring the variables
a = input("Enter no1:")
b = input("Enter no2:")
c = int(a)/int(b)

# Accessing them in print function
print("Division is:",c)
'''
'''
a = input("Enter no:")
b = input("Enter no:")
try:
    c = int(a)/int(b)
except Exception as e:
    print(f'Exception Occured: {e}')
    c = None
print(c)
'''
'''
a = input("Enter no:")
b = input("Enter no:")
try:
    c = int(a)/int(b)
except ZeroDivisionError as e:
    print(f'Division by zero exception: {e}')
    c = None
print(c)
'''
a = input("Enter no:")
b = input("Enter no:")
try:
    c = int(a)/int(b)
except ZeroDivisionError as e:
    print('Division by zero exception')
    c = None
except Exception as e:
    print('Exception Occured:',type(e).__name__)
    c = None
finally:
    print("Exicuting the finally clause")
print("Division is:",c)