from datetime import datetime

# definisikan input batas perhitungan tahun
# definisikan range bulan

tahun1 = int(input ("Tahun 1: "))
tahun2 = int(input("Tahun 2: "))
month1 = int(input("Bulan 1: "))
month2 = int(input("Bulan 2: "))

monday1 = 0

for year in range (tahun1, tahun2+1):
	for months in range (month1, month2+1):
		if datetime(year, months, 1).weekday() == 0:
			monday1 += 1

print ("Jumlah hari Senin dalam jangka pilihan user adalah ", monday1)


'''
#Atau bisa dibuatkan alternatif standar tanpa input dari user sebagai berikut:

from datetime import datetime

# definisikan input batas perhitungan tahun
# definisikan range bulan

monday1 = 0

for year in range (2015, 2017):
	for months in range (1, 13):
		if datetime(year, months, 1).weekday() == 0:
			monday1 += 1

print ("Jumlah hari Senin dalam jangka pilihan user adalah ", monday1)
'''