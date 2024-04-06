priceRange = [0, 50, 100, 500, 1000, 2500, 5000, 10000, 20000, 999999999999]
commitRange = [0, 50, 100, 500, 1000, 2500, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 999999999999]

price = 0

for j in range(len(priceRange)):
    if j == 0:
        if price <= priceRange[j]:
            print(j)
    else:
        if priceRange[j] >= price > priceRange[j - 1]:
            print(j)