print ("Hello World")

a = 1
b = 2
c = a + b
print (c)

if 5 > 2 :
	print ("Five is greater than two")

#third comment
x = "awesome"
print ("Python is " + x)

#fourth comment
x = 1
y = 2.8
z = 1j
print (type(x))
print (type(y))
print (type(z))

#Fifth comment
x = 1
y = 2.8
z = 1j
a = float (x)
b = int (y)
c = complex (x)
print (a)
print (b)
print (c)

print (type(a))
print (type(b))
print (type(c))

#Sixth comment
x = float (1)
y = float (2.8)
z = float ("3")
w = float ("4.2")
print (x)
print (y)
print (z)
print (w)
print (type(x))
print (type(y))
print (type(z))
print (type(w))

#Seventh comment
# z = "2 orang"
# a = int(z)
# print (a)

#Eighth comment
a = """Lorem Ipsum"""
print (a)

#Ninth comment
a = "Hello World"
print (a[2:4])

#Tenth comment
a = "Hello World"
print (a.replace("o","J"))

#Eleventh comment
a = "Selamat Pagi Wahai Manusia"
print (a.split (" ")[2])

#twelfth comment
age = 36
txt = "My name is John, and I am {}"
print (txt.format(age))
txt2 = "My age is {}"
print (txt2.format(age))

#thirteenth comment
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print (myorder.format(quantity, itemno, price))

#fourteenth comment
x =["apple", "banana"]
print ("semangka" not in x)

#fifteenth comment
fruit = "Papaya Melon Banana Apple"
print (len (fruit.split (" ")))

#Sixteenth comment
thislist = ["apple", "banana", "cherry"]
for x in thislist:
	print (x)

#seventeenth comment
thislist = ["apple", "banana", "cherry"]
thislist.pop (1)
print (thislist)

#eighteenth comment
thislist = ["apple", "banana", "cherry"]
print (thislist)

thislist = ["apple", "banana", "cherry"]
print (thislist[1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print (thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
	print (x)

thislist = ["apple", "banana", "cherry"]
thislist.insert (2,"mango")
print (thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove ("banana")
print (thislist)

#Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#if_else
a = 33
b = 200
if b > a:
  print("ab is greater than a")

#While Loop
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

adj = [1, 3, 6]
fruits = [1, 4, 8]

for x in adj:
  for y in fruits:
    print(x + y)

#nineteenth comment
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Functions
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#coy
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


#Function_Recursive
def my_function():
	print ("Hello from a function")
my_function()


#Calling_a_function
def my_function(fname, lname):
	print (fname + " Leonhart" + lname)
my_function ("Emil", " of Leningrad")
my_function ("Tobias", " of Leningrad")
my_function ("Linus", " of Bratislava")

#Default_Parameter_Value
def my_function(country = "Norway"):
	print("I am from " + country)
my_function ("Sweden")
my_function ("India")
my_function ()
my_function ("Brazil")

#Passing a List
def my_function(food):
	for x in food:
		print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return Values
def my_function(x):
	return 5 * x
print (my_function(3))
print (my_function(5))
print (my_function(9))

#Lambda
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))


#Lambda_Triple
def myfunc(n):
	return lambda a : a*n
mytripler = myfunc(3)
print(mytripler(11))
