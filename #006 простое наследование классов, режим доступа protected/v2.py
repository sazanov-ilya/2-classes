class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # Переопределяем в классе стандартный метод __str__
    def __str__(self):
        return f'({self.__x}, {self.__y})'

class Prop:
    def __init__(self, sp:Point, ep:Point, color:str = 'red', width:int = 1):
        print('Конструктор базового класса Prop')
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

class Line(Prop):
    def __init__(self, *args):
        print('Переопределенный конструктор Line')
        # Принудительно вызываем конструктор класса Prop
        # Prop.__init__(self, *args)
        # Правильнее вызывать через supper как
        super().__init__(*args)

    def drawLine(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')

class Rect(Prop):
    def drawRect(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')


l = Line( Point(1,2), Point(10,20) )
print(l._width)
l.drawLine()

r = Line( Point(30,40), Point(70,80) )
r.drawLine()

