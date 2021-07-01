# Пользовательский класс исключений error
class CoordError(Exception):
    pass

class ImageXIterator:
    def __init__(self, img, y:int):
        self.__limit = img.width
        self.__y = y
        self.__img = img
        self.__x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration

        self.__x += 1
        # возврашаем цвет координаты
        return  self.__img[self.__x-1, self.__y]


# Передирает строки
class ImageYIterator:
    def __init__(self, img):
        self.__limit = img.height
        self.__img = img
        self.__y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            raise StopIteration

        self.__y += 1
        # вызываем итератор по сторкам
        return ImageXIterator(self.__img, self.__y-1)




class Image:
    def __init__(self, width, height, background='_'):
        self.__background = background
        self.__pixels = {}  # Колекция координат точек, если цвет отличается от фона
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}  # Коллекция (словарь) уникальных цветов точек из __pixels

    @property  # Частное св-во для ширины
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property  # Частное св-во для высоты
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    # для доступа к отдельным пикселям переопределяем методы
    # __setitem__ и __getitem__
    def __checkCoord(self, coord):
        # Кортеж из 2-х элементов
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordError('Координаты точки должны быть двумерным кортежем')

        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            raise CoordError('Координаты выходят за пределы изображения')

    def __setitem__(self, coord, color):
        self.__checkCoord(coord)

        if color ==self.__background:
            # Если цвет равен цвету фора, удаляем пиксель из словаря
            self.__pixels.pop(coord, None)
        else:
            # В словарь добавляем пиксель с координатой и цветом
            self.__pixels[coord] = color
            # Добавляем цвет в палитру
            self.__colors.add(color)

    def __getitem__(self, coord):
        self.__checkCoord(coord)
        # возвращаем цвет координаты, если нет, то цвет фона (self.__background)
        return self.__pixels.get(coord, self.__background)

    def __iter__(self):
        # вызываем оператор по столбцам
        return  ImageYIterator(self)


class MyIter:
    def __init__(self, limit):
        self.__num = 0
        self.__limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration

        self.__num += 1
        return self.__num


img = Image(20, 4)
print ( img.width, img.height )

# __setitem__
img[1, 1] = '*'
img[2, 1] = '*'
img[3, 1] = '*'
# __getitem__
#color = img[5,4]
#for y in range(img.height):

#    for x in range(img.width):
#        print(img[x, y], sep='  ', end='')
#    print()

for row in img:
    for pixel in row:
        print(pixel, sep='  ', end='')
    print()

## MyIter
#it = MyIter(10)
#for i in it:
#    print(i)