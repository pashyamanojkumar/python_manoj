'''
Nested if statement
When you want to check for another condition after a condition resolves to true.
in such a situation, you can use the nested if construct.
if..elif..else
Syntax:
if expression1:
   statement(s)
   if expression:
      statement(s)
   else:
      statement(s)
elif expression:
   statement(s)
   if expression:
      statement(s)
   elif:
      statement(s)
   else:
      statement(s)
else :
   statement(s)
Examples:
mac_os = int(input("Enter value:"))
if mac_os < 200:
    print("Expression value is less than 200")
    if mac_os == 150:
        print("Which is 150")
    elif mac_os ==100:
        print("Which is 100")
    elif mac_os == 50:
        print("Which is 50")
elif mac_os < 50:
    print("Expression velue is less than 50")
else:
    print("Cloud not ind true expression")
print("Good bye!")
print("")
x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))
if x > y:
    if x > z:
        maximum = x
    else:
        maximum = z
else:
    if y > z:
        maximum = y
    else:
        maximum = z
print("The maximum value is:" + str(maximum))
'''
x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))
if x < y:
    if x < z:
        minimum = x
    else:
        minimum = z
else:
    if y < z:
        minimum = y
    else:
        minimum = z
print("The minimum value is:" + str(minimum))