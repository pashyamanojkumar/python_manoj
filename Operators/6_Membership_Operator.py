"""
In
Not in
# These are used to test whether a value or variable is found in a sequence
   (String, List, Tuple & Dictionary)
"""
x_value = 'Guido Van Rossum'
y_value = {1:'a',2:'b'}
print(x_value)
print(y_value)
print('Guido' in x_value)
print('guido' in x_value.lower())
Account_Name = input('Enter your Account Name :')
print(Account_Name)
a = input('Enter a value:')
print(a in x_value.lower())

print(1 in y_value)
print('b' in y_value)
print('R' in x_value)
print('R' not in x_value)