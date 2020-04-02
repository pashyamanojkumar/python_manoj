#!/usr/bin/python
# Integer,float and complex
'''int()
float()
complex()'''
raw_Data=5
print(raw_Data,type(raw_Data),id(raw_Data))
print(isinstance(raw_Data,int))
float_Data=5.84
print(float_Data,type(float_Data),id(float_Data))
print(isinstance(float_Data,float))
complex_Data=8 + 4j
print(complex_Data,type(complex_Data),id(complex_Data))
print(isinstance(complex_Data,complex))
print(isinstance(complex_Data,int))

# Mathematical Functions : +, -, /, *, %, <, >, <=, =>
# Built-in Methods:
# 1. abs() : 0-9 +ve distance b/w n to zero
print(abs(-30))
# 2. ceil() : the smallest integer not less than x value
import math
print(math.ceil(62.1))
print(math.ceil(-62.1))
