def iki_tamsayi_al():
    while True:
        try:
            sayi1 = int(input("Birinci tam sayıyı girin: "))
            sayi2 = int(input("İkinci tam sayıyı girin: "))
            sonuc = sayi1 / sayi2
            print("Sonucun tam sayı kısmı:", int(sonuc))
            break
        except ValueError:
            print("Hatalı giriş! Lütfen tam sayı girin.")
        except ZeroDivisionError:
            print("Hata! Sıfıra bölme yapılamaz. Lütfen farklı bir sayı girin.")

iki_tamsayi_al()