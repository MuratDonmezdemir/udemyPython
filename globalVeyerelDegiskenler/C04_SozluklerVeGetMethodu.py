super_lig = {"galatasaray": "63 puan", "fenerbahce": "62 puan", "besiktas": "61 puan"}

takim = input("Lütfen puan durumunu öğrenmek istediğiniz takımı giriniz: ").strip().lower()

if takim not in super_lig:
    print("Bu takımın puan durumu bulunamadı.")
else:
    puan = super_lig[takim]
    print(f"{takim.capitalize()}: {puan}")
