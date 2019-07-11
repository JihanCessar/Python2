'''
import json

x = {
	"name": "John",
	"age": 30,
	"married": True,
	"divorced": False,
	"children": ("Ann", "Billy"),
	"pets": None,
	"cars": [
		{"model": "BMW 230", "mpg": 27.5},
		{"model": "Ford Edge", "mpg": 24.1}
	]
}

# use four indents to make it easier to read the result:

print(json.dumps(x, indent=4))
'''

'''
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
'''


'''
import re

#check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
	print ("Yes! We have a match!")
else:
	print*"No Match"
'''

'''
import re

str = "The rain in Spain falls mainly in the plain!"

# Check if the string contains "ai" followed by 1 or more "x" character:

x = re.findall("aix+", str)

print (x)

if (x):
	print ("Yes, there is at least one match!")
else:
	print ("No match")
'''

'''
import re

str = "The rain is Spain."
x = re.search("\s", str)

print ("The first white-space character is located in position:", x.start())
'''

'''
import re

str = " The rain in Spain."

#check if "ain" is present at the beginning of a word:

x = re.findall("\A ", str)

print (x)

if (x):
	print ("Yes, there is at least one match!")
else:
	print("No match")
'''

'''
import re

str = "18 times before 11:45 AM"

# Check if the string has any two-digits numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", str)

print(x)
if (x):
	print("Yes, there is at least one match")
else:
	print("No match")
'''

'''
import re

str = "The rain in Spain"

#Check if the string starts with "The":

x = re.split("\AThe", str)

print(x)

if (x):
  print("Yes, there is a match!")
else:
  print("No match")
'''

'''
import re

# split the string at the first white-space character:

str = "The rain in Spain"
x = re.split("\s", str, 2)

print (x)'''


'''
import re

#Replace all white-space characters with the digit "9":

str = " The rain in Spain"
x = re.sub("\s", "", str, 1)
print(x)
'''

import re

# search for an upper case "S" character in the beginning of a word, and print its position:

str = "The ZSain in Spain"

x = re.findall(r"\b\w+", str)
print (x)