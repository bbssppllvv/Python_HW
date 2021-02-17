currentResult = int(input("Current Result - "))
goal = int(input("Goal - "))
counter = 1

while currentResult < goal:
    print(counter,"Day - ", currentResult)
    counter = counter + 1
    currentResult = round(currentResult * 1.1, 2)
else:
    print("Sportsman will reach the goal", currentResult, "in", counter, "days", )
