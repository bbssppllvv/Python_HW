with open("3.txt", "r") as file:
    employees = {line.split()[0] : float(line.split()[1]) for line in file}
    print("Average:", round(sum(employees.values()) / len(employees)))
    print("Less then 20000:", [e[0] for e in employees.items() if e[1] < 20000])
