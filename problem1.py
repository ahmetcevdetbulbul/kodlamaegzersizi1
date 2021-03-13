liste=list()
for i in range(100):
    liste.append(i)
sayi=list()

for i in liste:

    if i<10:
        sayi.append(i)

    else:
        liste1 = list()
        a=i

        while a>=10:
            b=a%10
            liste1.append(b)
            a=a//10
        liste1.append(a)
        liste1.reverse()

        for i in liste1:
            sayi.append(i)


