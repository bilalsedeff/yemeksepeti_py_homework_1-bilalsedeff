initial_sentence = str(input("Harflerinin değiştirilmesini istediğiniz metni giriniz: "))

devam = True

while devam == True:
    cevap = True
    degisecek_harf = str(input("Hangi harfin değişmesini istiyorsunuz?: "))
    degistirilecek_harf = str(input("Bu harfin, hangi harf ile değiştirilmesini istiyorsunuz?: "))

    if str(degisecek_harf) in str(initial_sentence):
        if len(degisecek_harf) == 1 and len(degistirilecek_harf) == 1:
            initial_sentence = initial_sentence.replace(degisecek_harf, degistirilecek_harf)
            print("Sonuç: " + initial_sentence)
            while cevap == True:
                cevap = input("Devam etmek istiyor musunuz? (E/H): ")
                if cevap.lower() == "e":
                    cevap = False
                    continue
                elif cevap.lower() == "h":
                    cevap = False
                    devam = False
                else:
                    print("Lütfen geçerli bir cevap veriniz")
                    cevap = True
        else:
            print("Lütfen bir adet harf giriniz")
            continue
    else:
        print("Bu harf, cümlenin içinde bulunmamaktadır, lütfen tekrar deneyiniz")
        continue
