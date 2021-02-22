file = open("2.txt", "r")
lines = 0
words = 0

for line in file:
    lines += 1
    words += len(line.split())
file.close()
print(lines)
print(words)
