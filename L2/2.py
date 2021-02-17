x = [int(x) for x in input("Введите числа через пробел - ").split()]

count = 0
length = len(x)
m = len(x) % 2

if m == 0:
    print("В списке ЧЕТНОЕ кол-во элементов")
    while count < length:
        x[count], x[count + 1] = x[count + 1], x[count]
        count += 2
else:
    print("В списке НЕЧЕТНОЕ кол-во элементов")
    length -= 1
    while count < length:
        x[count], x[count + 1] = x[count + 1], x[count]
        count += 2

    print(x)
