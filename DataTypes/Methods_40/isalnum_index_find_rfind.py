a='8'
b="ab"
c="Python5.3"
d=' '
print(a.isalnum())
print(b.isalnum())
print("calling c variable: ", c.isalnum())
print(d.isalnum())

print("")
str1="Its Python world....wow!!!"
str2='Python'
print(str1.index(str2))
print(str1.index(str2,0))
print(len(str1))
print(str1.index(str2,0,20))

str1="this abc is really a string example....wow!!!"
str2='is'
print(str1.find(str2))
print(str1.find(str2,0,10))
print(str1.find(str2,10,40))
print('')
print(str1.rfind(str2))
print(str1.rfind(str2,0,11))
print(str1.rfind(str2,10,0))
print("")

samplaeData=" & "
sequence=("a","b","c")
print(samplaeData,type(samplaeData),id(samplaeData),len(samplaeData))
print(sequence,type(sequence),id(sequence),len(sequence))
print(samplaeData.join(sequence))
print("")

