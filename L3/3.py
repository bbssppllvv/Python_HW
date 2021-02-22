def my_func(a, b, c):
    data = [a, b, c]
    data.remove(min(data))
    return sum(data)

a, b ,c = 12, 7, 12
print(my_func(a, b ,c))