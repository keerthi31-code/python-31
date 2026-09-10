price = 40
people = [20, 15, 5, 1]

people.sort(reverse=True)

count = 0

for money in people:
    if money <= price:
        price = price - money
        count += 1

    if price == 0:
        break

print(count)