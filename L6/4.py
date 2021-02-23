class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"New car {self.name}, Color {self.color}, Police - {self.is_police}")

    def go(self):
        print(f"{self.name}: Car is driving")
    def stop(self):
        print(f"{self.name}: Car is stopped")
    def turn(self, direction):
        print(f"{self.name}: Car is turned {'left' if direction == 0 else 'right'}")
    def show_speed(self):
        print(f"{self.name}: Car speed is {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}: Speed - {self.speed} - Over speed!"\
            if self.speed > 40 else f"{self.name}: Speed - {self.speed}"


class Sportcar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar("Lada", "Blue", 100)
police_car.go()