# Объекты-свойства (property)
class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if (isinstance(x, int) or isinstance(x, float)):
            return True
        return False

    @property
    def coordX(self):
        print('Вызов __getCoords')
        return self.__x

    @coordX.setter
    def coordX(self, x):
        print('Вызов __setCoords')
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError('Неверный формат данных')

    @coordX.deleter
    def coordX(self):
        print('Удаление свойства')
        del self.__x

    # Объект-свойство
    #coordX = property(__getCoords, __setCoords, __delCoordX)


pt = Point(1, 2)
pt.coordX = 100  # запись значения
x = pt.coordX  # чтение значения
print(x)

del pt.coordX
#pt.coordX  # Ошибка свойства __x в экземпляре класса нет

pt.coordX = 50  # Снова сождает свойство __x в экземпляре класса pt
print( pt.coordX )





