'''
is and is not are the identity operators
are used to check if two values or variables are located on the same part of the memory
'''
x1 = 5
y1 = 5
print(x1, id(x1))
print(y1, id(y1))
print(x1 is y1)
print(x1 is not y1)
print("")
x2 = 'ManojREDDY'
y2 = "ManojREDDY"
print(x2,id(x2),y2,id(y2))
print(x2 is y2)
print("")
x3 = [1,2,3,4]
y3 = [1,2,3,4]
print(x3,id(x3),y3,id(y3))
print(x3 is y3)
print(x3 is not y3)
print("")
a1 = (1,2,3,4)
b1 = (1,2,3,4)
print(a1,b1,id(a1),id(b1))
print(a1 is b1)
print(a1 is not b1)