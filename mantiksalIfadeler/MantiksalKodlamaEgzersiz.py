vize_not = int(input("Vize Notunuzu Giriniz: "))
final_notu = int(input("Final notunuzu Giriniz: "))

ortalama_al = (final_notu + vize_not) / 2

if ortalama_al >= 85:
    print("Tebrikler AA aldınız..", ortalama_al)
elif ortalama_al >= 65:
    print("Tebrikler BB aldınız.. :", ortalama_al)
elif ortalama_al >= 50:
    print("Tebrikler CC aldınız.. :", ortalama_al)
else:
    print("Maalesef ders tekrarı.....", ortalama_al)
