file = open("1.txt", "w")

while True:
    data = input("Введите данные - ")
    file.write(f"{data} \n")
    if data == "":
        file.close()
        break
