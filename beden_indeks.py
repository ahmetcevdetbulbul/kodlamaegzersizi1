#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

print("şimdi beden kütle indeksinizi hesaplıcaz.")
boy = float(input("lüten boyunuzu giriniz:"))
kilo = int(input("lütfen kilonuzu giriniz:"))

indeks = kilo / (boy * boy)
print("vucut kütle indeksiniz:{}".format(indeks))

if indeks <= 18.5 :
    print("Zayıf")
elif 18.5 < indeks <= 24.9 :
    print("Normal kilolu")
elif 24.9 < indeks <= 29.9 :
    print("Fazla kilolu")
else :
    print("OBEZ!!")

