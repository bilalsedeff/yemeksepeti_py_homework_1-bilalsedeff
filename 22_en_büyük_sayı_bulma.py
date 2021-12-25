sayılar = [4, 53, 22, 64, 3, 2, 72, 45, 56, 60]

büyük = 0

for i in range(len(sayılar)):
    if sayılar[i] > int(büyük):
        büyük = sayılar[i]
    else:
        continue


print(büyük)
