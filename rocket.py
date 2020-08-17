from math import sqrt

class Rocket():

    def __init__(self, x=0, y=0, fuel_level=100, name="SpaceX"):
        self.x = x
        self.y = y
        self.fuel_level = fuel_level
        self.name = name

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        self.fuel_level = self.fuel_level - self.x - self.y

    def get_distance(self, other_rocket):
        distance = sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2)
        return distance

rocket_0 = Rocket(name="Vinit")
rocket_0.move_rocket(1, 1)
rocket_1 = Rocket(10, 5)

print(rocket_0.name, rocket_0.get_distance(rocket_1), rocket_0.fuel_level)

#Vinit Shah