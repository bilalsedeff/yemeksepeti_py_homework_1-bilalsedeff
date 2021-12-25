import string


metin = "Bu haftaki eğitimin GÜZEL geçeceğini umuyorum"
büyük = 0
küçük = 0


for i in metin:
    if i in string.ascii_lowercase:
        küçük =+ 1
    elif i in string.ascii_uppercase:
        büyük =+ 1
    else:
        continue

print("Büyük: ", büyük, "\n", "Küçük: ", küçük)
