db_ka = "admin"
db_ps = 1234

while True:
    kullanici_adi = input("Lütfen Kullanıcı Adı Giriniz: ")
    kullanici_ps = int(input("Lütfen Şifrenizi Giriniz: "))

    if db_ka == kullanici_adi and db_ps == kullanici_ps:
        print("*** Hoşgeldiniz ***:", kullanici_adi)
        break
    elif db_ka != kullanici_adi:
        print("Kullanıcı adı hatalı.")
    elif db_ka == kullanici_adi and db_ps != kullanici_ps:
        print("Şifreniz hatalıdır.")
        cevap = input("Şifre değiştirilsin mi? (E/H): ")
        if cevap.upper() == "E":
            yeniSifre = int(input("Lütfen yeni şifrenizi yazınız: "))
            db_ps = yeniSifre
            print("Şifreniz başarıyla değiştirildi.")
        else:
            print("Kullanıcı adı ve şifre hatalıdır.")
