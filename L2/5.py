# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating = [20, 16, 16, 11, 9, 9, 8, 7, 6, 5, 5]
input = int(input("Enter any number - "))
count = 0

for i in rating:
    if i < input:
        rating.insert(count, input)
        print("Rating Updated")
        break
    elif count == len(rating) - 1:
        rating.append(input)
        print("Добавил в конец")
        break
    count +=1


print(rating)