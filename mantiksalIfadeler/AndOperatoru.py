from multiprocessing.connection import answer_challenge

from KarsilastirmaOperatorleri.EsittirOperatoru import kullani_sifre
from KarsilastirmaOperatorleri.karsilastirma import kontrol
from s01_kullanicidanVeriAlma import kullanici_adi

deneme  =8<10 and 15<12
print(deneme)


print("-------")

db_ps =1234
db_ka ="murat"
kullanici_adi =input("lütfen kullanici adinizi giriniz:")

kullani_sifre=int (input("lutfen sifrenızı giriniz:"))
kontrol =db_ps == kullani_sifre and db_ka == kullanici_adi
print(kontrol)
