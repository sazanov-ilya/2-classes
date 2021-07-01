class Point:
    x = 1
    y = 2

    def setCoords(self, x, y):
        self.a = x
        self.b = y

pt1 = Point()
pt1.setCoords(5, 10)
print( pt1.__dict__ )
# экввивалент
Point.setCoords(pt1, 11, 22)
print( pt1.__dict__ )

pt2 = Point()
pt2.setCoords(50, 100)
print( pt2.__dict__ )