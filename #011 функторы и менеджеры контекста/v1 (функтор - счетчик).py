# функторы - объекты классов, которые можно выполнять как функции
# класс счетчик
class Counter:
    def __init__(self):
        self.__counter = 0

    # для вызова как функцию
    def __call__(self, *args, **kwargs):
        self.__counter += 1
        print(self.__counter)
        return self.__counter


с1 = Counter()
c2 = Counter()
# вызываем как функцию
с1()
с1()
c2()