'''
A ser is an unordered collection without duplicates
when printed, iterated upon, or converted into a sequence,
it's elements will appears in an arbitrary,implementation-dependent order.

'''
a=set()
print(a,type(a),id(a))
abc= set(('a','b','a','b'))
print(abc,type(abc),id(abc))

#abc= set(['a','b','c','d'])
#print(abc,type(abc),id(abc))
#adict=set({'Name':'Guido Van Rossum','Language':'Python',1:10})
adict=set({1:10,2:20})
print(adict,type(adict),id(adict))