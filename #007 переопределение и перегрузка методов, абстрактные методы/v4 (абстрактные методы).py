class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # Переопределяем в классе стандартный метод __str__
    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def isDigit(self):
        if (isinstance(self.__x, int) or isinstance(self.__x, float)) and \
                (isinstance(self.__y, int) or isinstance(self.__y, float)):
            return True
        return False

    def isInt(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False

class Prop:
    def __init__(self, sp:Point, ep:Point, color:str = 'red', width:int = 1):
        # print('Конструктор базового класса Prop')
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def setCoords(self, sp, ep):
        if sp.isDigit() and ep.isDigit():
            self._sp = sp
            self._ep = ep
        else:
            print('Координаты должны быть числами')

    def draw(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод draw()')


#class Line(Prop):
#    def drawLine(self):
#        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#    def __setOneCoord(self, sp):
#        if sp.isInt():  # Если sp целое число
#            self._sp = sp
#        else:
#            print('Координата должна быть целым числом')
#
#    def __setTwoCoord(self, sp, ep):
#        # self._sp = sp
#        # self._ep = ep
#        # Вызываем setCoords бвзового класса Prop
#        Prop.setCoords(self, sp, ep)
#
#    def setCoords(self, sp: Point, ep: Point = None):
#        if ep is None:  # Если нет параметра ep
#            #  Выносим в частный вспомогательный метод setOneCoord
#            #if sp.isInt():  # Если sp целое число
#            #    self._sp = sp
#            #else:
#            #    print('Координата должна быть целым числом')
#            self.__setOneCoord(sp)
#        else:  # Иначе проверяем обе координвты
#            if sp.isInt() and ep.isInt():
#                #self._sp = sp
#                #self._ep = ep
#                # Вызываем setCoords бвзового класса Prop
#                #Prop.setCoords(self, sp, ep)
#                self.__setTwoCoord(sp, ep)
#            else:
#                print('Координаты должны быть числами')

# Создаем вспомогательные объекты с одноименным методом
class Line(Prop):
    def draw(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')


class Rect(Prop):
    def draw(self):
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')


class Elipse(Prop):
    def draw(self):
        print(f'Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}')


#l = Line( Point(1,2), Point(10,20) )
#l.draw()
#r = Rect( Point(1,2), Point(100,200) )
#r.draw()
#e = Elipse( Point(1,2), Point(-10,-20) )
#e.draw()

# Помещаем объекты в коллекцию
figs = []
figs.append( Line( Point(1,2), Point(10,20)) )
figs.append( Rect( Point(1,2), Point(100,200)) )
figs.append( Elipse( Point(1,2), Point(-10,-20)) )

for f in figs:
    f.draw()
