sayı_listesi = []
state = True
tekler = []
çiftler = []

while state == True:
    sayi = input("Lütfen bir sayı giriniz:")
    sayı_listesi.append(int(sayi))
    if len(sayı_listesi) == 10:
        state = False
    else:
        continue

for i in range(len(sayı_listesi)):
    if sayı_listesi[i]%2 == 0:
        çiftler.append(sayı_listesi[i])
    else:
        tekler.append(sayı_listesi[i])

print("Çiftler: ", çiftler)
print("Tekler: ", tekler)
