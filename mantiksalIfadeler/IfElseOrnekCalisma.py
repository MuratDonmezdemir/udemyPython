sut_miktari = int (input("lütfen süt miktarini yaziniz  :"))
kasar_peyniri_siniri =11
if sut_miktari< kasar_peyniri_siniri:
    print("süt miktariniz kasar peyniri icin uygun degıl :",sut_miktari     )
    print("kasar peynırı uretmek ıcın ihtiyacınız olan sut mıktari:",(kasar_peyniri_siniri-sut_miktari))

else :
    toplam_uretim =sut_miktari/kasar_peyniri_siniri
    print(f"toplam uretim :{ int(toplam_uretim)}")
