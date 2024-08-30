
for i in range(3):
     sifre =input("lutfen sıfre belırleyınız :" )

     if not  sifre:
         print("bu alan bos bırakılamaz....")

     elif len(sifre) in range(3,8)   :
         print("yenı sıfrenız",sifre)
         break

     elif i ==2:
         print("şifreyi 3 defa yanlıs gırdınız lutfen 15 dakıka bekleyınız")


     else:
         print("sıfre 8 karakterden uzun yada 3 karakterden kısa")
