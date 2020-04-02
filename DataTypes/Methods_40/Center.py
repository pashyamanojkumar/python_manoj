#!/usr/bin/python

abc_string_1 = "abcdef"
abc_string = """abcd \
tools \
py \
"""
print("abc_string_1.center(10, K) : ", len(abc_string_1), abc_string_1.center(11, '&'))
print("abc_string.center(10, 'J') :", len(abc_string), abc_string.center(30, 'J'))