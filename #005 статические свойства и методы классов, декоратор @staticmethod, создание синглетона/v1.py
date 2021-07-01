class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        # Накапливаем счетчик
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    def getCount(self):
        return Point.__count


pt1 = Point()
pt2 = Point()
pt3 = Point()
print( pt1.getCount())
