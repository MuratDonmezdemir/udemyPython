

import random

kullanicilar = []

def kullanici_Ekle(x):
    print("-" * 30)
    print("Kullanıcı ekleme ekranına hoş geldiniz....")

    ekle = input("Lütfen eklenecek kullanıcıyı yazınız: ")
    x.append(ekle)
    input("Devam etmek için enter tuşuna basınız....")

def kullanici_gor(x):
    print("-" * 30)

    if len(x) == 0:
        print("Hiç kullanıcı eklenmedi.")
    else:
        say = 1
        for i in x:
            print(f"{say} - Kullanıcı adı: {i}")
            say += 1

    print("-" * 30)
    input("Devam etmek için enter tuşuna basınız....")

def sec(x):
    print("-" * 30)
    kisi_sec = int(input("Kaç kişi seçilsin? : "))

    if kisi_sec > len(x):
        print("Seçilecek kişi sayısı mevcut kullanıcı sayısından fazla olamaz.")
    else:
        rastgele_sec = random.sample(x, kisi_sec)
        say = 1
        for i in rastgele_sec:
            print(f"{say} - Kullanıcı adı: {i}")
            say += 1

    print("-" * 30)
    input("Devam etmek için enter tuşuna basınız....")

def salla(x):
    print("-" * 30)
    random.shuffle(x)
    say = 1
    for i in x:
        print(f"{say} - Kullanıcı adı: {i}")
        say += 1

    print("-" * 30)
    input("Devam etmek için enter tuşuna basınız....")

while True:
    print("*** ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ ***")
    secim = int(input("1 - Kullanıcı Ekle\n2 - Kullanıcı Gör\n3 - Kullanıcı Karıştır\n4 - Rastgele Seç\n5 - Çıkış\nSeçiminiz: "))

    if secim == 1:
        kullanici_Ekle(kullanicilar)
    elif secim == 2:
        kullanici_gor(kullanicilar)
    elif secim == 3:
        salla(kullanicilar)
    elif secim == 4:
        sec(kullanicilar)
    elif secim == 5:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Lütfen uygun bir tercih yapınız...")
