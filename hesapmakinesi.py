print("""

[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Bölme
[5] Üs Alma
[0] Çıkış

	""")
giris=input("Yapmak istediğiniz işlemi seçiniz : ")

if giris=="1":
	x=input("Birinci sayı : ")
	x=float(x)
	y=input("İkinci sayı : ")
	y=float(y)
	print("Toplam = ",x+y)
elif giris=="2":
	x=input("Birinci sayı : ")
	x=float(x)
	y=input("İkinci sayı : ")
	y=float(y)
	if x>y:
		print("Fark = ",x-y)
	elif x<=y:
		print("Fark = ",y-x)
elif giris=="3":
	x=input("Birinci sayı : ")
	x=float(x)
	y=input("İkinci sayı : ")
	y=float(y)
	print("Çarpım = ",x*y)
elif giris=="4":
	x=input("Bölünen : ")
	x=float(x)
	y=input("Bölen : ")
	y=float(y)
	if y!=0:
		print("Bölüm = ",x/y)
	else:
		print("Bölüm  = tanımsız")
elif giris=="5":
	x=input("Taban : ")
	x=float(x)
	y=input("Kuvvet : ")
	y=int(y)
	print("Sonuç = ",x**y)
elif giris=="0":
	print("Programdan çıkılıyor...")
	quit()
else:
	print("Hatalı giriş yaptınız!")
	quit()