metin = input("Lütfen bir metin giriniz: ")

def karakter_yazdirma(sentence):
    sentence = sentence.replace(" ", "")
    ilk_iki = sentence[0:2]
    son_iki = sentence[-2:]
    print(ilk_iki+son_iki)

karakter_yazdirma(metin)
