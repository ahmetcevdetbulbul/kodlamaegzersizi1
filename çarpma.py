#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

a1 = int(input("lütfen 1. sayıyı girin:"))
a2 = int(input("lütfen 2. sayıyı girin:"))
a3 = int(input("lütfen 3. sayıyı girin:"))

sonuç = a1*a2*a3
print("{}x{}x{}={}".format(a1,a2,a3,sonuç))
