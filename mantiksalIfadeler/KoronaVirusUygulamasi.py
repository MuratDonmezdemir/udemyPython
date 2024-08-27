ates_durumu = float(input("Lütfen Ateş derecenizi giriniz: "))

oksuruk = input("Öksürüğünüz var mı? (E/H): ").lower()
bas_agrisi = input("Baş ağrınız var mı? (E/H): ").lower()
gun = int(input("Şikayetleriniz kaç gündür var?: "))

if ates_durumu >= 39:
    if gun >= 3:
        print("****Uyarı: Hastaneye gidiniz...")
    else:
        print("Ateş durumunuz sınırda. Devam ederse hastaneye gidiniz...")
else:
    print("Ateş durumunuz normal.")
