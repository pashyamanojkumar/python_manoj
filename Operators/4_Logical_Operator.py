# Logical Operator
'''
and logical AND
or logical OR
not logical NOT
'''
'''
import keyword
print(keyword.kwlist)

Output: 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
 'return', 'try', 'while', 'with', 'yield']
'''
x = True
y = False
print(x and y) # Both True then only True
print(x or y)  # If one can True then true
print(not y)   # If x True Then O/P True