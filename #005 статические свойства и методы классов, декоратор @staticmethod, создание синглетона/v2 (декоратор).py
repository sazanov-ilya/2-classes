class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        # Накапливаем счетчик
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    # Декортор указания статического метода
    # после этого в методе не нежно указачать параметр self
    @staticmethod
    def getCount():
        return Point.__count


def getCount():
    return 5


pt1 = Point()
pt2 = Point()
pt3 = Point()

# переприсвоение метода getCount в эеземпляре класса pt1
pt1.getCount = getCount

print( pt1.getCount(), pt2.getCount(), Point.getCount())

