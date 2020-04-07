"""
Decision making is anticipation of condition occurring while execution of the
program and specifying actions taken to the conditions.

Decision structures evaluate multiple expressions which produce TRUE or FALSE
as outcomes.
1. simple if
2. if..else
3. elif
4. nested elif
"""
# simple if
course_name = 'Python'
if course_name:
    print("1 - Got a true expression value")
print("Welcome to python world")

course_name = input("enter your course: ")
if course_name == 'Python':
    print("1 - Got a true expression value")
print("Welcome to python world")

course_name = input("enter your course: ")
course = "Python"
if course_name == course.lower():
    print("1 - Got a true expression value")
print("Welcome to python world")

course_name = input("enter your course: ")
course = "Python"
if course_name.lower() == course.lower(): print("Welcome to Python class")

