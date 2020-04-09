'''
import os
print(os.getcwd())
print(os.system("/"))
print(os.environ)
print(os.getpid())
print(os.getgid())
print(os.listdir("/Users/manoj/python_manoj/File_And_Dir"))
print(os.uname())
#print(os.remove())
'''
'''
python file operators
1. Open a file
2. Read or Write
3. Close the file

# Builtin Functions
1. open()
Example: var.read() or var.write()

2. close() 
'''
"""
file = open("abc.txt")
print(file.read())
file.close()
...........................:
'r' - Open a file for reading.(default)
'w' - Open a file for writing. Creates a new file if it does not exist
      or truncates the file if it exists.
'x' - Open a file for exclusive creation.
            if the file already exists, the operation fails.
'a' - Open for appending at the end of the file without truncating it.
't' - Open in text mode.(default)
'b' - Open in binary mode.
'+' - Open a file for updating (reading and writing)
"""


