# Bitwise Operator
"""
& : Bitwise And
| : Bitwise Or
~
^
>>
<<
"""
''''# 192.168.0.3
print(bin(192))
print(bin(168))
print(bin(0))
print(bin(3))
'''
# 1 = True
# 2 = False

a = 15
b = 10
print(bin(a))
print(bin(b))
'''
0b1111
0b1010
-------
  1010
'''
print(bin(a&b))
'''
0b1111
0b1010
-------
  1111
'''
print(bin(a|b))
'''
0b1111
0b1010
-------
  0101
  
1+1 = 0
1+0 = 1
'''
print(bin(a^b))
