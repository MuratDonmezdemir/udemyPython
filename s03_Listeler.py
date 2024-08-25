

listeler =["murat"," dönmezdemir", "bilişim"]


print(len(listeler))# listenin uzunluğunu
print(listeler)#listenin içindeki elementleri yazdırır
print (listeler[1])# 1. nci index teki element i yazdırır yani dönmezdemir index sıfırdan baslar



listeler.append("programlama")#listenin sonuna programlama yazdırır



listeler[2]="SQl programlama"# 2 . indexteki element i 'bilişimi' , 'SQL' ile degiştirdi

print(listeler)

print(listeler[:2]) # sıfırıncı ve birinci index si alır
                    #'murat ,dönmezdemir ' yazdırır


listeler[:2] =["Galatasaray ,sk"]# "murat dönmezdemiri " galatasaray  sk" olarak degiştirdik
print(listeler) #['Galatasaray ,sk', 'SQl programlama', 'programlama']

print(listeler[0:2])#sıfırdan 2 . elemente kadar yazdırır