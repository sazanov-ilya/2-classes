class Point:
    def __init__(self, x=0, y=0):
        print('Создание экземпляра класса Point:')
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление зкземпляра: '+self.__str__())
        

pt1 = Point()
pt2 = Point(5)
pt3 = Point(5, 10)

print(pt1.__dict__, pt2.__dict__, pt3.__dict__, sep='\n')

