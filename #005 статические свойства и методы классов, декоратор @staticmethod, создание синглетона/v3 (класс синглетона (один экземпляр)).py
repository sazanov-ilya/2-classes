class Point:
    __count = 0
    __instance = None

    # Перегруженная ф-ия создания нового экземпляра класса
    def __new__(cls, *args, **kwargs):
        # cls --> Point
        # Если класс Point не имеет экземпляров --> __instance = None
        if not isinstance(cls.__instance, cls):
            # Создаем новый экзкмпляр класса Point
            # И присваиваем __instance имя нового созданного экземпляра
            cls.__instance = super(Point, cls).__new__(cls)
        else:
            print('Экземпляр класса уже создан!')

    def __init__(self, x=0, y=0):
        # Накапливаем счетчик
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    # Декортор указания статического метода
    # после этого в методе не нежно указачать параметр self
    @staticmethod
    def getCount():
        return Point.__count


def getCount():
    return 5


pt1 = Point()
pt2 = Point()
pt3 = Point()

print( id(pt1), id(pt2), id(pt3), sep='\n' )

