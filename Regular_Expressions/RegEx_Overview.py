
"""
import re
line = '''Welcome to Python World by Manoj Reddy'''
search_Object = re.search('Python',line,re.M|re.I)
if search_Object:
    message = search_Object.group()
else:
    message = "Pattern doesn't exist"
print(f"{message}")

# r'expression'
# R'expression'
# .(a period)  -- matches any single character except newline '\n'

# match_Object = re.match(pattern='Python',string=line, flags=re.M|re.I)
# match_Object = re.match(r'(.*)Python(.*)',string=line, flags=re.M|re.I)
match_Object = re.match(r'(.*)Python(.*?)',string=line, flags=re.M|re.I)

if match_Object:
    message = match_Object.group()
else:
    message = "Pattern doesn't exist"
print(f"Searching for pattern python: {message}")
.......
import re
data = '810-394-8097 # This is a Phone Number'
num = re.sub(r'#.*$',"",data)
print(f"Phone Number Is: {num}")
num1 = re.sub(r'\D',"",data)
# \D is match a non digit:[0-9]
print(num1)
.........
import re
text = 'abbaaabbbbaabbbaaabb'
pattern = 'bba'
for match in re.findall(pattern,text):
    print(f"Found Match {match}")
...................
import re
pattern = 'this'
text = 'Does this text match the pattern?'
print(text.index('this'))
match = re.search(pattern,text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ("%s")' % (match.re.pattern, match.string, s, e, text[s:e]))
print(f"Start index {s} and End index {e} in a given {text} {text[s:e]}")
"""
import re
raw_data = "june 12 august 8 jan 12"
#1. Lets usa a regular expression to match a few data strings.
regex = r"[a-zA-Z]+ \d+"
# \d   -- decimal digit [0-9]
# []  Matches
matches = re.findall(regex,raw_data,re.M|re.I)
for match in matches:
    print("Full match: %s" % (match))

#2. To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex,"june 12 august 8 jan 12")
for match in matches:
print("Match month: %s" % (match))

#3. If we need the exact position of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex,"june 12 august 8 jan 12")
for match in matches:
    print("Match at index: %s, %S" % (match))
