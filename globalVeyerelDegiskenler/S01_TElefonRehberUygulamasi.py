# Global telefon rehberi sözlüğü
tel_rehberi = {}

def tel_no_ekle():
    print("***** NUMARA EKLEME EKRANINA HOŞGELDİNİZ *****")
    numara_isim_al = input("Lütfen kayıt edilecek kişinin adını yazınız: ").strip()
    numara_no_al = input("Lütfen telefon numarasını giriniz: ").strip()

    tel_rehberi[numara_isim_al] = numara_no_al
    print(f"{numara_isim_al} adlı kişi telefon rehberine eklendi.")

def tel_rehber_goster():
    kisi_sayisi = len(tel_rehberi)
    print(f"Rehberdeki kayıtlı kişi sayısı: {kisi_sayisi}")
    print("Rehberinize hoşgeldiniz!")
    if not tel_rehberi:
        print("Rehberde kayıtlı kişi bulunmuyor.")
    else:
        for isim, numara in tel_rehberi.items():
            print(f"{isim}: {numara}")

def no_sil():
    print("Kişi silme ekranına hoş geldiniz...")
    silinecek_kisi = input("Silinecek kişiyi yazınız: ").strip()

    if silinecek_kisi in tel_rehberi:
        tel_rehberi.pop(silinecek_kisi)
        print(f"{silinecek_kisi} rehberden silindi.")
    else:
        print(f"{silinecek_kisi} rehberde bulunamadı.")

while True:
    print("*** HOŞGELDİNİZ ***")
    print("*** SEÇİM YAPINIZ ***")
    secim_yap = int(input("1- Ekle\n2- Sil\n3- Rehberi Gör\n4- Çıkış\n"))

    if secim_yap == 1:
        tel_no_ekle()
    elif secim_yap == 2:
        no_sil()
    elif secim_yap == 3:
        tel_rehber_goster()
    elif secim_yap == 4:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Lütfen uygun bir tuşa basınız...")
