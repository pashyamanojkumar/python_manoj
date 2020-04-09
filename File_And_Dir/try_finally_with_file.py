'''
try:
    statement(s)
finally:
    statement()

try:
    file = open("abc.txt",'r+')
    print(file.readline())
    print(file.readlines())
finally:
    file.close()

# with statement:
with open("abc.txt",'r') as myfile:
    #print(myfile.read())
    print(myfile.readline())
    #print(myfile.readlines())
'''
import os
try:
    file = open("abc.txt")
    print(file.read())
    print(file.tell())
    print(file.seek(0))
    print(file.readline())
    print(file.tell())
    print(file.seek(0))
    print(file.readlines())
    print(file.tell())
    print(file.seek(0))
    
finally:
    f.close()
