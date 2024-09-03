
def su_hesapla():
    kilo = input("Lütfen kilonuzu giriniz: ")

    # Kilonun sayısal bir değer olup olmadığını kontrol edelim
    if not kilo.isdigit():
        print("Geçersiz kilo girdiniz. Lütfen sayısal bir değer giriniz.")
        return

    kilo = int(kilo)  # Kilo değerini tam sayıya dönüştürelim
    erkek_hesapla = kilo * 0.04
    kadin_hesapla = kilo * 0.03
    cinsiyet = input("Lütfen cinsiyetinizi giriniz...kadın/erkek: ").lower()

    if not cinsiyet:
        print("Bu alan boş bırakılamaz.")
    elif cinsiyet == "erkek":
        print(f"{erkek_hesapla:.2f} litre su içmelisiniz...")
    elif cinsiyet == "kadın":
        print(f"{kadin_hesapla:.2f} litre su içmelisiniz...")
    else:
        print("Geçersiz cinsiyet girdiniz. Lütfen 'kadın' veya 'erkek' giriniz.")

# su_hesapla fonksiyonunu çağırarak işlemi başlatıyoruz
if __name__ == "__main__":
    su_hesapla()
