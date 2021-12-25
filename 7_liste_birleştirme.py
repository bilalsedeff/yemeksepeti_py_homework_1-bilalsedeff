liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

liste1.extend(liste2)

print("Extend metodu ile: ", liste1)

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

print("+ operatörü ile: ", liste1+liste2)

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

for i in liste2:
    liste1.append(i)

print("append metodu ile: ", liste1)
