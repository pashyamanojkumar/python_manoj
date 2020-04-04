'''tuple1=('Python',"AWS","Azure",1991,20.84)
print(tuple(enumerate(tuple1)))
# del
del tuple1(1)
print(tuple1)
'''
# min_max
tuple1, tuple2=('123','xyz','manu',"sri"),(400,600,80,44,842)
print("min value element: ",min(tuple1))
print("max value element: ",max(tuple1))
print("min value element: ",min(tuple2))
print("max value element: ",max(tuple2))

# update
tup1=(1,3,5)
tup2=('a','b','c')
print(tup1)
print(tup2)
tup3=tup1+tup2
print(tup3)
