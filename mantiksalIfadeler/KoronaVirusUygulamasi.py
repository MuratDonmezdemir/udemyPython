ates_durumu = float(input("Lütfen Ateş derecenizi giriniz: "))

oksuruk = input("Öksürüğünüz var mı? (E/H): ").lower()
bas_agrisi = input("Baş ağrınız var mı? (E/H): ").lower()
gun = int(input("Şikayetleriniz kaç gündür var?: "))

if ates_durumu >= 39:
    if gun >= 3:
        print("****Uyarı: Hastaneye gidiniz...")
    else:
        print("Ateş durumunuz sınırda. Devam ederse hastaneye gidiniz...")
if (ates_durumu>=39) and (oksuruk =="e") and (bas_agrisi =="e") and (gun>=3):
    print("******ACİL En Yakın Saglık Kurulusuna Gidiniz !!!!")
    print("*****ACİL Durumunuz Olumlu Görünmüyor !!!")

elif(ates_durumu<=39)or (oksuruk =="e") or(bas_agrisi =="e") or (gun>=3):
    print("Durumunuz bu sekılde devam ederse Lutfen saglık kurulusuna bas vurunuz....")
