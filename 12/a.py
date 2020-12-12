input = open("12/input.txt", "r").read()

# input = """
# F10
# N3
# F7
# R90
# F11
# """

instructions = [(i[0], int(i[1:])) for i in input.strip().split("\n")]

import math

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = (1,0)

    def move(self, dir, amount):
        if dir == "N":
            self.y += amount
        if dir == "E":
            self.x += amount
        if dir == "W":
            self.x -= amount
        if dir == "S":
            self.y -= amount
        if dir == "F":
            self.x += amount * self.direction[0]
            self.y += amount * self.direction[1]
        if dir == "L":
            self.turn(-amount)
        if dir == "R":  
            self.turn(amount)

    def turn(self, deg):

        newdirection = self.rotate((0,0), self.direction, math.radians(360-deg))
        self.direction = newdirection

    def rotate(self, origin, point, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.

        The angle should be given in radians.
        """
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return round(qx), round(qy)
    
    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

ship = Ship()

for instruction in instructions:
    dir,amount = instruction
    ship.move(dir, amount)

print(abs(ship.x) + abs(ship.y))