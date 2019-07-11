#inisiasi input nilai temperatur dan
#pemilihan perhitungan konversi
c = input("Masukkan nilai temperatur: ")
d = input ("(1) untuk konversi C ke F atau \n(2) untuk konversi F ke C \nPilih konversi: ")

#perhitungan konversi
if int(d) <= 1 :
	print ("Konversi nilai temperatur anda adalah "+str(((9/5)*int(c)+32))+" F")
else :
	print ("Konversi nilai temperatur anda adalah "+str((int(c)-32)*(5/9))+" C")
		