profit = int(input("Enter Company Gross Profit - $"))
costs = int(input("Enter Company Costs - $"))

if profit - costs > 0:
    print("Company Profit - $", profit - costs)
    employees = int(input("Enter number of employees in the company - "))
    print("Every Employee Get  - $", (profit - costs)/employees)
else:
    print("Your company is not profitable, your balance is $",  profit - costs)