# Объект Line должен принимать только целочисленные координаты
# Остальные объекты - могут также вещественные
# Для этого переопределяем setCoords в объекте Line

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


class Line(Prop):
    def drawLine(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')

    def __setOneCoord(self, sp):
        if sp.isInt():  # Если sp целое число
            self._sp = sp
        else:
            print('Координата должна быть целым числом')

    def __setTwoCoord(self, sp, ep):
        # self._sp = sp
        # self._ep = ep
        # Вызываем setCoords бвзового класса Prop
        Prop.setCoords(self, sp, ep)

    def setCoords(self, sp: Point, ep: Point = None):
        if ep is None:  # Если нет параметра ep
            #  Выносим в частный вспомогательный метод setOneCoord
            #if sp.isInt():  # Если sp целое число
            #    self._sp = sp
            #else:
            #    print('Координата должна быть целым числом')
            self.__setOneCoord(sp)
        else:  # Иначе проверяем обе координвты
            if sp.isInt() and ep.isInt():
                #self._sp = sp
                #self._ep = ep
                # Вызываем setCoords бвзового класса Prop
                #Prop.setCoords(self, sp, ep)
                self.__setTwoCoord(sp, ep)
            else:
                print('Координаты должны быть числами')

#class Rect(Prop):
#    def drawRect(self):
#        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}')


l = Line( Point(1,2), Point(10,20) )
l.drawLine()
l.setCoords( Point(10, 20), Point(100, 200) )
l.drawLine()
l.setCoords( Point(-10, -20) )
l.drawLine()

# r = Line( Point(30,40), Point(70,80) )
# r.drawLine()

