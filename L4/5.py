from functools import reduce

data = [el for el in range(100, 1001) if el % 2 == 0]
print(data)

def summary(prev_el, el):
    return prev_el * el

print(reduce(summary, data))