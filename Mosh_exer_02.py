# Write a function
# that returns the maximum of two numbers.


def angkaPalingBesar(x,y):
	if x > y:
		return x
	elif y > x:
		return y
	else:
		return "pilihan anda ternyata sama, bro!"


a = int(input("Masuk cuy: "))
b = int (input("Lagi cuy: "))

print (angkaPalingBesar(a,b))