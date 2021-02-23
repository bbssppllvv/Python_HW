from time import sleep


class TrafficLight:
    __color = "off"

    def running(self):
        self.color = "red"
        print(self.color)
        sleep(7)
        self.color = "yellow"
        print(self.color)
        sleep(2)
        self.color = "green"
        print(self.color)
        sleep(3)


a = TrafficLight()
a.running()