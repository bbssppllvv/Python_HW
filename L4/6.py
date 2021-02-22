from itertools import count, cycle
number = int(input("Ввведите начальное число - "))

for el in count(number):
    if el > number + 15:
        break
    else:
        print(el)

x = 0
for el in cycle("ABC"):
    if x > 15:
        break
    else:
        x += 1
        print(el)