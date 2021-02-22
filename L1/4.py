number = int(input("Введите целое число - "))
last_nimber = number % 10 # получаем последнюю цифру
x = 0

while  number / 10 > 0:
    prew_nimber = number % 10  # получаем последнюю цифру
    number = int(number / 10)  # убираем одну цифру с конца

    prew_nimber = number % 10

    if  prew_nimber > last_nimber:
        last_nimber = prew_nimber

print("Наибольшее число = ", last_nimber)

