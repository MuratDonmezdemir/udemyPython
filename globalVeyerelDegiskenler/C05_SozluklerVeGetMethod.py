


super_lig = {"galatasaray": "63 puan", "fenerbahce": "62 puan", "besiktas": "61 puan"}

takim = input("Lütfen puan durumunu öğrenmek istediğiniz takımı giriniz: ").capitalize().strip()


print(takim,",",super_lig.get(takim ,"bu takım listede yok "))
