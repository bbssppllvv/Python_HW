class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def full_name(self):
        return f"{self.name} {self.surname}"
    def full_profit(self):
        return f"{sum(self._income.values())}"

staff = Position("Alex", "Block", "Poet", 20000, 10000)
print(staff.full_name())
print(staff.position)
print(staff.full_profit())