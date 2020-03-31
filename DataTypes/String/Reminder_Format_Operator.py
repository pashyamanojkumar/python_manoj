#!/usr/bin/python
#str1 = "Hello World!"
#str2 = 'This is an example String'
firstname = "Manoj"
middleName = "Reddy"
LastName = "Pashya"
 #formatting of strings
'''print("your name is %s and your account id is %d" %("pashyamanojkumar",52049))
print("")
print("FIRST NAME:", firstname, "MIDDLE NAME:", middleName, "LAST NAME:",LastName)
print("")
print("FIRST NAME: %s, MIDDLE NAME: %s, LAST NAME: %s" %(firstname,middleName,LastName))'''
# {} = place Holders
print("FIRST NAME: {}, MIDDLE NAME: {}, LAST NAME: {}" .format(firstname,middleName,LastName))
print("FIRST NAME: {2}, MIDDLE NAME: {0}, LAST NAME: {1}" .format(firstname,middleName,LastName))
print("Full Name: {} , Account ID: {}".format("PashyaManojReddy",8103948097))
print("First Name: {}, Last Name: {} , Account ID: {}".format("ManojReddy","Pashya",8103948097))
print("First Name: {0}, Last Name: {1} , Account ID: {2}".format("ManojReddy","Pashya",8103948097))


"""print("calling str1 {0} and calling str2 {1}".format(str1,str2))
print("Value1 {} Value2 {} and Value3 {}".format("python",100,"PyCharm"))
print("Value1 {1} Value2 {0} and Value3 {2}".format("python",100,"PyCharm"))"""
print("Value1: {a}, Value2: {b}, and Value3: {c}".format(a="python",b=100,c="PyCharm"))