data = input('Enter words separated with spaces - ')
list_index = data.count(" ")
data = data.split()
count = 0

while list_index > count:
    print(data[count][:10])
    count += 1
