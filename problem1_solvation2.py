list = list()

for i in range(1,1000):
    if i < 10:
        list.append(i)
    elif 100 > i >= 10:
        a = i // 10
        list.append(a)
        a1 = i % 10
        list.append(a1)
    elif 1000 > i >= 100:
        x = i//100
        x1 = i//10
        x2 = i % 10
        list.append(x)
        list.append(x1)
        list.append(x2)

print(list)



