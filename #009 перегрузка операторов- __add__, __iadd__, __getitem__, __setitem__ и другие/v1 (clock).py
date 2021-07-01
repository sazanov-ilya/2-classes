class Clock:
    __DAY = 86400  # Число секунд в дне
    def __init__(self, secs:int):
        if not isinstance(secs , int):
            raise ValueError('Секунды должны быть целым числом')

        # гарантирует что __secs не будет превышать __DAY
        self.__secs = secs % self.__DAY

    def getFormatTime(self):
        s = self.__secs % 60            # часы
        m = (self.__secs // 60) % 60    # минуты
        h = (self.__secs // 3600) % 24  # секунды
        return f'({Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)})'

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else '0'+str(x)


c1 = Clock(100)
c2 = Clock(200)
# c3 = c1 + c2  # ошибка
print( c1.getFormatTime() )






