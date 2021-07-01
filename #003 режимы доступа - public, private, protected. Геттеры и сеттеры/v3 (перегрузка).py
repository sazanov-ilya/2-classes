class Point:
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

    def __getattribute__(self, item):
        '''Вызывается при получении свойства класса с именем item'''
        if item == '_Point__x':
            # При попытке получить атрибут x подмена его значения
            return 'Частная переменная'
        else:
            # Обязательно для работы с остальными атрибутами
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        '''Вызывается при изменениее свойства key класса'''
        if key == 'WIDTH':
            # При попытке сменить значение атрибута WIDTH, генерируем ошибку
            raise AttributeError
        else:
            # Обязательно для работы с остальнымиатрибутами
            self.__dict__[key] = value

    def __getattr__(self, item):
        '''Вызывается при получении несуществующего свойства item класса'''
        print('__getattr__: '+item)

    def __delattr__(self, item):
        '''Вызывается при удалении свойства item (неважно есть оно или нет)'''
        print('__delattr__: '+item)


pt = Point(1, 2)

# Попытка изменить свойство WIDTH
#pt.WIDTH = 5  # Исключение AttributeError

# Попытка обратиться к несуществующему свойству
pt.zzz

# Удаление свойства
pt.z = 1
del pt.z



