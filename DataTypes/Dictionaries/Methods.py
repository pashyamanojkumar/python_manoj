
'''Dict_1 = {'Name':'srilatha','Age':26,'Class':'Masters'}
print(Dict_1,type(Dict_1),id(Dict_1),len(Dict_1),dict(enumerate(Dict_1)))
Dict_1['Age']=25
print(Dict_1)
Dict_1['School']='IGlobalUniversity'
print(Dict_1)
print(Dict_1['Name'])

# del Dict_1
# del Dict_1['Name']

Dict_1.clear()
print(Dict_1)

# get()
dict1= {'Name':'srilatha','Age':26,'Class':'Masters'}
print(dict1['Name'])
print(dict1.get('Name'))
print(dict1.get('srilatha'))
print(dict1.get('FirstName','Pashya'))
print("")

# key()
print(dict1.keys())

# values()
print(dict1.values())
print("")

# items()
print(dict1.items())
print("")

# copy()
_DICT= {'Name':'srilatha','Age':26,'Class':'Masters'}
print(_DICT,id(_DICT))
newDict= _DICT.copy()
print(newDict,id(newDict))
print("")

# fromkeys()
account=('Name','Address','AccountNumber')
a=dict.fromkeys(account)
print(a)
b=dict.fromkeys(account,8)
print(b)
print("")
'''
# setdefault()
Dict_001= {'Name':'srilatha','Age':26,'Class':'Masters'}
print(Dict_001.setdefault('Age',None))
print(Dict_001.setdefault('Course','Python')
'''
Dict_002= {'Data':'Raw','id':8}
Dict_001.update(Dict_002)
print(Dict_001)
'''