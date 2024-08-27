boy = float(input("Boyunuzu metre cinsinden giriniz (örn: 1.75): "))
kilo = float(input("Kilonuzu kilogram cinsinden giriniz: "))

vki = kilo / (boy ** 2)

print(f"Vücut Kitle İndeksiniz: {vki:.2f}")

if vki < 18.5:
    print("Zayıf kategorisindesiniz.")
elif 18.5 <= vki < 24.9:
    print("Normal kiloda kategorisindesiniz.")
elif 25 <= vki < 29.9:
    print("Fazla kilolu kategorisindesiniz.")
else:
    print("Obez kategorisindesiniz.")
