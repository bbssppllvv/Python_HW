def my_func(x, y):
    print("Result #1 ", x**y)

    count = 1
    result = x
    while -y > count:
        result = result * x
        count += 1
    print("Result #2 ", 1/result)

x, y = 4, -8
my_func(x, y)