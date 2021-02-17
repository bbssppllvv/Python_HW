# a = ['11','12','13', '14']
input = input("Enter month number - ")

#Data
data_list = ['winter', "spring", "summer","autumn" ]
data_dic = {"winter": ["1", "2", "12"], "spring": ["3", "4", "5"], "summer": ["6", "7", "8"], "autumn": ["9", "10", "11"]}

#For list
if int(input) <= 2 or int(input) == 12:
    print("[list] It is winter")
elif int(input) > 2 and int(input) < 6 :
    print("[list] It is spring")
elif int(input) >= 6 and int(input) < 9 :
    print("[list] It is summer")
elif int(input) >= 9 and int(input) < 12 :
    print("[list] It is autumn")
else:
    "[list] Error, enter correct month number"

#For dictionary
for a, b in data_dic.items():
    count = 0
    while count < 3:
        if b[count] == input:
            print("{Dictionary} It is", a)
            break
        count += 1

if int(input) > 12:
    print("{Dictionary} Error, enter correct month number")
