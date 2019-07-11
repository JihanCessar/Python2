'''
class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def say_hi(self):
        print('Hello, my name is {}. \nMy address is in {}. \nMy age is {}.'.format(self.name, self.address, self.age))


p = Person('Swaroop','Mampang','55')
del p.age
p.say_hi()
print (p.say_hi())

p2 = Person('Hadoop','Bogor', '22')
p2.age = 88
p2.say_hi()


# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
'''


'''
class Robot:
	"""Represents a robot, with a name."""
	# A class variable, counting the number of robots
	population = 0


	def __init__(self, name):
		"""Initializes the data."""
		self.name = name
		print ("(Initializing {})".format(self.name))

		# Whenthis person is created, the robot
		# adds to the population
		Robot.population += 1

	def die(self):
		"""I am dying."""
		print ("{} is being destroyed!".format(self.name))

		Robot.population -= 1

		if Robot.population == 0:
			print ("{} was the last one.".format(self.name))
		else:
			print ("There are still {:d} robots working.".format(Robot.population))

	def say_hi (self):
		"""Greeting by the robot.

		Yeah, they can do that."""
		print ("Greetings, my masters call me {}.".format(self.name))

	@classmethod
	def how_many(cls):
		"""Prints the current population."""
		print ("We have {:d} robots.".format(cls.population))

droid1 = Robot ("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot ("C-3PO")
droid2.say_hi()
Robot.how_many()

print ("\nRobots can do some work here.\n")

print ("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
'''


'''
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)


class Student(Person):
	def __init__(self, fname, lname, year):
		Person.__init__(self, fname, lname)
		self.graduationyear = year

# Use the Person class to create an object, and execute the printname method:

x = Student ("Mike", "Olsen", 2010)
print(x.graduationyear)
'''


'''
class SchoolMember:
	"""Represents any school member."""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print ("(Initialized SchoolMember: {})".format(self.name))

	def tell(self):
		"""Tell my details"""
		print ('Name: "{}" Age: "{}"'.format(self.name, self.age), end=" ")

class Teacher (SchoolMember):
	"""Represents a teacher"""
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print ('Initialized Teacher: "{}"'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary: "{}"'.format(self.salary))


class Student(SchoolMember):
	"""Represents a student."""
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student: "{}")'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividiya', 40, 30000)
s = Student('Swaroop', 25, 75)

#print a blank line

print ()

members = [t, s]
for member in members:
	#works for both Teachers and Students
	member.tell()
'''

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")