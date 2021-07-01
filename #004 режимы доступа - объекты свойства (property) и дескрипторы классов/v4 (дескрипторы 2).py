# Дескриптор это класс со специальными методами
class CoordValue:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        # instance ссылается на экземпляп класса и в нем создает коллекцию __dict__
        instance.__dict__[self.__name] = value


class Point:
    # Создаем дескрипторы и передаем имена для локальных переменных
    coordX = CoordValue('coordX')
    coordY = CoordValue('coordY')

    def __init__(self, x=0, y=0):
        # У дескриптора эта операция является перегруженной и
        # фактически вызывает метод __set__ класса CoordValue и записывает  значение
        # в атрибут __value класса Point, не создавая локальных атрибутов в классе pt
        self.coordX = x
        self.coordY = y


pt1 = Point(1, 2)
pt1.coordX = 5
pt2 = Point(10, 20)
print(pt1.coordX, pt1.coordY)
print(pt2.coordX, pt2.coordY)
# Но тут фактически ссылка на атрибуты родительского класса
#print( id(pt1.coordX), id(Point.coordX))






