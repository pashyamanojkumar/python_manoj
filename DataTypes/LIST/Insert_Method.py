#!/usr/bin/python
data_01=["superman","spiderman",1991,1993,1991,"Spiderman"]
onemorelist=[22,34,56,34,34,78,98]
print(list(enumerate(data_01)))
data_01.insert(0,"Django")
print(list(enumerate(data_01)))
data_01.insert(6,"Google")
print(list(enumerate(data_01)))
print("")

# remove()
aList=["superman","spiderman",1991,1993,1991,"Spiderman"]
onemoreList=[22,34,56,34,34,78,98]
print(aList,list(enumerate(aList)))
aList.remove(1991)
print(aList,list(enumerate(aList)))
aList.remove('superman')
print(aList,list(enumerate(aList)))
aList.remove("DevOps")
print(aList,list(enumerate(aList)))
print('')
