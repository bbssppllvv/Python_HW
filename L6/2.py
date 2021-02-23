class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def get_full_profit(self):
        return f"{self._length}m * {self._width} * 25kg * 5sm = {(self._length * self._width * 25 * 5) / 1000}t"

road = Road(500, 20)
print(road.get_full_profit())