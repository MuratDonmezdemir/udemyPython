def sayilari_topla():
    sayilar = []

    while True:
        girdi = input("Bir sayı girin (Çıkmak için 'Q'ya basın): ")

        if girdi.lower() == 'q':
            break

        try:
            sayi = float(girdi)
            sayilar.append(sayi)
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.")

    toplam = sum(sayilar)
    adet = len(sayilar)

    print(f"Girilen sayı adedi: {adet}")
    print(f"Girilen sayıların toplamı: {toplam}")


sayilari_topla()