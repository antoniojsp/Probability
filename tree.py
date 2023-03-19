class Balls:
    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number


class Box:
    def __init__(self, balls: list[Balls], chances: float):
        self.balls = {i.get_color(): i.get_number() for i in balls}
        self.chances = chances
        self.number = sum(self.balls.values())

    def get_chances(self, color: str):
        return self.balls[color] / self.number * self.chances


a = Box([Balls("Red", 7), Balls("Blue", 8)], 0.9)
print(a.get_chances("Red"))
b = Box([Balls("Red", 7), Balls("Blue", 3)], 0.1)
print(b.get_chances("Red"))

print(a.get_chances("Red") + b.get_chances("Red"))
