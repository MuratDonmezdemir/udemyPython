db_ps =1234
db_ka ="murat"
kullanici_adi =input("lütfen kullanici adinizi giriniz:")

kullani_sifre=int (input("lutfen sifrenızı giriniz:"))
kontrol =db_ps == kullani_sifre or db_ka == kullanici_adi
print(kontrol)
