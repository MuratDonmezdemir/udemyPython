


super_lig = {"galatasaray": "63 puan", "fenerbahce": "62 puan", "besiktas": "61 puan"}

takim_Ekle =input("Takım Giriniz:")
puan_Ekle =input("puan giriniz :")

super_lig.setdefault(takim_Ekle,puan_Ekle)



for  isim ,deger in super_lig.items():
    print(isim,deger)
