seconds = int(input("Enter seconds - "))

m = seconds // 60
s = seconds % 60
h = m // 60
m = m % 60

print(f'{h:d}:{m:02d}:{s:02d}')