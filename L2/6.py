goods = {"название":"", "цена":"", "количество":"", "eд":"" }
analitics = {"название":[], "цена":[], "количество":[], "eд":[]}

while True:
    if input(f"Введите q для выхода Enter для продолжения- ") == "q":
        break
    for i in goods.keys():
        data = input(f"Введите {i} - ")
        if data == "q":
            break
        if i == "цена" or i == "количество":
            data = int(data)
        goods[i] = data
        analitics[i].append(goods[i])

    print(f"\nТовары\n {goods}")
    print(f"\nАналитика\n {analitics}\n\n")