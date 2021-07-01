class Point:
    WIDTH = 5
    # Список разрешенных свойств экземпляров класса (именно экземпляров)
    __slots__ = ['__x', '__y', 'z']

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if (isinstance(x, int) or isinstance(x, float)):
            return True
        return False


    def setCoords(self, x, y):
        '''Сеттер'''
        if (Point.__checkValue(x) and Point.__checkValue(y)):
            self.__x = x
            self.__y = y
        else:
            print('Координаты должны быть числом')

    def getCoords(self):
        '''Геттер'''
        return self.__x, self.__y


pt = Point(1, 2)

# Ошибка надо добавить в список разрешенных свойств
pt.z = 1




