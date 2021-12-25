metin = str(input("Lütfen bir kelime giriniz: "))

def palindrom_checker(sentence):
    if sentence == sentence[::-1]:
        print("Bu palindrom bir kelimedir")
    else:
        print("Bu palindrom bir kelime değildir")

palindrom_checker(metin)
