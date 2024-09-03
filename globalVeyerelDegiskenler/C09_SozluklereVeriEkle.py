super_lig = {"galatasaray": "63 puan", "fenerbahce": "62 puan", "besiktas": "61 puan"}

while True:
    # Kullanıcıdan takım ve puan bilgilerini al
    takim = input("Takım ekleyiniz: ").strip()
    puan = input("Puan ekleyiniz: ").strip()

    # Takım ve puan bilgilerini sözlüğe ekle
    super_lig[takim] = puan

    # Sözlükteki tüm anahtar ve değerleri yazdır
    print("\nGüncellenmiş Süper Lig Puan Durumu:")
    for takim_adi, puan_durumu in super_lig.items():
        print(f"{takim_adi.capitalize()}: {puan_durumu}")

    # Döngüyü bitirmek için bir çıkış koşulu ekleyin
    devam = input("\nDevam etmek ister misiniz? (E/H): ").strip().lower()
    if devam != 'e':
        print("Çıkış yapılıyor...")
        break
