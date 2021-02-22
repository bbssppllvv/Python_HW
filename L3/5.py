def sum():
    x = 0
    while True:
        input_num = input("Введите числа через пробел или q для выхода - ").split()

        for i in input_num:
            if i == "q":
                print("Программа завершена")
                return
            else:
                x += int(i)
        print("Сумма чисел =", x)

sum()
