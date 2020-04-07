'''
1. Required Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Arguments

# 1. Required Arguments
# Creating of a Function
def hello(a):
    print(a)
    return

# Creating of a Variable
abc = 'Welcome to Python World'

# Accessing/Calling of a Function
hello(abc)

# 2. Keyword Arguments
def hello1(abc):
    print(abc)
    return

# Accessing/Calling of a Function
hello1(abc="Pashya Reddy")

def data(name,age):
    print(f"Name : {name}")
    print(f"Age : {age}")
    return
data(name="Pashya Manoj Reddy", age=28)

# 3. Default Arguments
def data(name,age=35):
    print(f"Name : {name}")
    print(f"Age : {age}")
    return
data(name="Pashya Manoj Reddy", age=28)

def data(name,age=35):
    print(f"Name : {name}")
    print(f"Age : {age}")
    return
data(name="Manoj Reddy")
'''
# 4. Variable-Length Arguments
def info(var1, *vartuple):
    print(var1)

    for i in vartuple:
        print(i)
    return
info(10,20,30,40,50,60,70,80,90)
