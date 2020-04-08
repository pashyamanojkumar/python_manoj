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