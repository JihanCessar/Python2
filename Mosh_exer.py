# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.



def fizz_buzz(x):
	if x%3 ==0 and x%5 !=0:
		return "Fizz"
	elif x%5 ==0 and x%3 !=0:
		return "Buzz"
	elif x%3 ==0 and x%5 ==0:
		return "Fizz Buzz"
	else:
		return "Sorry, gan! Ane balikin tuh angka " + str(x)

j = int(input("Masuppin angka agan: "))
print (fizz_buzz(j))