class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Styles:
    def __init__(self, color='red', width=1):
        print('Конструктор Styles')
        self._color = color
        self._width = width


class Pos:
    # *args - остаточные аргументы
    def __init__(self, sp:Point, ep:Point, *args):
        print('Конструктор Pos')
        self._sp = sp
        self._ep = ep
        # Передаем остаточные *args в конструктор второго класса Styles
        Styles.__init__(self, *args)


class Line(Pos, Styles):
    def draw(self):
        print( f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}' )


l = Line( Point(10,10), Point(100,100), 'griin', 5 )
l.draw()