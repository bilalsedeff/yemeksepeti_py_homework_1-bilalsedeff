sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

removed_spaces = { x.translate({32:None}) : y
                 for x, y in sozluk.items()}

print(removed_spaces)

sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}


removed_spaces = {x.replace(' ', '') for x, v in sozluk.items()}

print(removed_spaces)
