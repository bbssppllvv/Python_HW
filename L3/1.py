data = input("Enter two numbers - ").split()
a, b = data

def divider(a, b):
    if b == "0":
        print("Не ноль не делим")
        return
    print(int(a)/int(b))
    return

divider(a, b)