class Clock:
    __DAY = 86400  # Число секунд в дне
    def __init__(self, secs:int):
        if not isinstance(secs , int):
            raise ValueError('Секунды должны быть целым числом')

        # гарантирует что __secs не будет превышать __DAY
        self.__secs = secs % self.__DAY

    def getFormatTime(self):
        s = self.__secs % 60            # секунды
        m = (self.__secs // 60) % 60    # минуты
        h = (self.__secs // 3600) % 24  # часы
        return f'({Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)})'

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else '0'+str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):  # перегрузка сложения - c1 + c2
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типа Clock()')

        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):  # перегрузка +=
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типа Clock()')

        self.__secs += other.getSeconds()
        return self

    def __eq__(self, other):  # перегрузка сравнения ==
        return self.__secs == other.getSeconds()
        #if self.__secs == other.getSeconds():
        #    return True
        #return False

    def __nq__(self, other):  # перегрузка !=
        # инвертируем __eq__
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Ключ должен быть строкой')

        if item == 'hour':
            return (self.__secs // 3600) % 24
        elif item == 'min':
            return (self.__secs // 60) % 60
        elif item == 'sec':
            return self.__secs % 60

        return 'неверный ключ'

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ должен быть строкой')

        if not isinstance(value, int):
            raise ValueError('Значение должно быть числом')

        # Вычисляем текущее значения
        s = self.__secs % 60            # секунды
        m = (self.__secs // 60) % 60    # минуты
        h = (self.__secs // 3600) % 24  # часы

        if key == 'hour':
            # сек и мин не меняем, но добавляем часы
            self.__secs = s + 60 * m + value * 3600
        elif key == 'min':
            # сек и часы ме меняем, но добавляем минуты
            self.__secs = s + 60 * value + h * 3600
        elif key == 'sec':
            # меняем секунды, а часы и мин без изменений
            self.__secs = value + 60 * m + h * 3600


c1 = Clock(100)
c2 = Clock(100)
c3 = c1 + c2
print( c3.getFormatTime() )

c4 = c1 + c2 + c3
print( c4.getFormatTime() )

c1 += c2
print(c1.getFormatTime())

if c1 == c3:
    print('время равно')

if c1 != c4:
    print('время не равно')

print( c1['hour'], c1['min'], c1['sec'])

c1['hour'] = 10
print(c1.getFormatTime())




