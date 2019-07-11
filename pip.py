'''
import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print (c.hump(txt))

# This meethod capitalizes the first letter of each word.
'''

'''
# The try block will generate an error because x is not defined:

try:
	print(x)
except:
	print("An exception occured, boss")
	'''

'''
try:
	print (x)
except NameError:
	print("Variable x is not defined")
except:
	print("Somethng else went wrong")

'''

try:
	f = open("demofile.txt")
	f.write("Lorum Ipsum")
except:
	print("Something went wrong when writing to the file.")
finally:
	f.close()