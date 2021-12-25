num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

sort_orders = sorted(num.items(), key=lambda x: x[1], reverse=False)

for i in sort_orders:
	print(i[0], i[1])
