from pydoc import stripid

sil ="++++murat++++".strip("+") # sadece + leri siler
print (sil) # murat yazdirir
  # yada aşağıdaki gibi de yapabiliriz


print (sil.strip("t")) # t harfini sildik mura yazdırır

print ("murat","dönmezdemir",sep="+")# , yerine + işareti koyduk


print ("murat","dönmezdemir",sep=":")# , yerine : işareti koyduk

print ("kişinin adı " , end=":")#  kişinin adi : şeklinde yazdırır
                                # metnin sonuna : işareti eklemek için kullanırız