#Exercise 1
#Sorting input user
n = input("Masukkan userkey: ")
print ("Your userkey is "+n)
#sortasi tiap alfabet, angka, dan simbol
count1=0
count2=0
count3=0

for i in n:
	if i.isalpha() == True:
		count1+=1
	elif i.isnumeric() == True:
		count2+=1
	else:
		count3+=1
print ("Jumlah huruf = "+str(count1))
print ("Jumlah angka = "+str(count2))
print ("Jumlah simbol = "+str(count3))
