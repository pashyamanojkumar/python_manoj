import sys
#file = open("/users/manoj/python_manoj/abc.txt")
import os
# print(os.getcwd())
# print(os.listdir("/Users/manoj/python_manoj/Exception_Handling"))
# print(os.uname())
print(os.getpid())
'''
for i in file:
    try:
        file = open(i,'r')
    except Exception as e:
        print('Can not open',e)
    else:
        print(i,'has',len(file.readline()),'lines')
        file.close()
'''
'''
import sys
assert ("linux" in sys.platform),"This code runs on linux only"

try:
    statement # Run this code
except:
    statement # Execute this code when there is an exception
'''
'''
import sys
def platform_check():
     assert ("linux" in sys.platform),"This function code runs on linux only"
     print("Hi,Welcome to Python")
try:
    platform_check()
except AssertionError as error:
    print(error)
    print("f platform_check function was not executed")
else:
    print("Executing the code")
'''
import sys
def platform_check():
     assert ("linux" in sys.platform),"This function code runs on linux only"
     print("Hi,Welcome to Python")
try:
    platform_check()
except AssertionError as error:
    print(error)
    print("f platform_check function was not executed")
else:
    print("Executing the code")
finally:
    print(" I am a finally Block")




