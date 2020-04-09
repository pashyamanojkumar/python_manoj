file = open("abc.txt")
# print(file.read())
# file.write("Python was created/developed/invented by Guido Van Rossum")

print(file.tell()) # Initial curser position
print(file.read())
print(file.tell()) # After curser position
print(file.seek(0)) # bring curser positionto 0
print(f"Reading a Line : {file.readline()}")
print(f"Remaining Lines : {file.readlines()}")
file.close()
#print(file.read())
