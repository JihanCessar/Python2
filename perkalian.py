#Exercise 2
#Masukan angka yang diinginkan
n = input("Masukkan angka: ")
print ("Angka anda adalah: " + n)

#Angka yang dimasukkan kemudian akan dikalikan
#dengan perkalian 1 hingga 10
i=1
while i <= 10:
	print (str(i)+"x"+n+"="+str(i*int(n)))
	i+=1
