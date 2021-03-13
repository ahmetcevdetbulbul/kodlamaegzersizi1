# 2. dereceden bir bilinmeyeli bir denkelmin köklerini bulma

print("ax^2+bx+c denklem formatımız\nlütfen katsayıları tam sayı belirleyelim" )

a = int(input("lütfen a değerini belirleyin:"))
b = int(input("lütfen b değerini belirleyin:"))
c = int(input("lütfen c değerini belirleyin"))

delta = b*b - 4 * a * c

x1 = -b - delta**0.5 / 2*a

x2 = -b + delta**0.5 / 2*a

print("ilk kök:{}\nikinci kök:{}".format(x1,x2))