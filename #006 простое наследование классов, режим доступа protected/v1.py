class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # Переопределяем в классе стандартный метод __str__
    def __str__(self):
        return f'({self.__x}, {self.__y})'

class Line:
    # sp:Point - нотация, что ожидается передача в качестве параметра объекта Point
    # :str - будем передавать строку
    # Нотацияы - это подсказка, передавать можно что угодно
    def __init__(self, sp:Point, ep:Point, color:str = 'red', width:int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._widht = width

    def drawLine(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._widht}')

class Rect:
    def __init__(self, sp:Point, ep:Point, color:str = 'red', width:int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._widht = width

    def drawRect(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._widht}')


# все классы изначально наследуются от базового класса object
print( issubclass(Point, object) )

l = Line( Point(1,2), Point(10,20) )
l.drawLine()

r = Line( Point(30,40), Point(70,80) )
r.drawLine()


# Дублюрующий код Классов Line и Rect выносим в отдельный класс
# v2
