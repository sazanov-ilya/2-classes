## файловый поток
#fp = None
#try:
#    fp = open('myfile.txt')
#    for t in fp:
#        print(t)
#except Exception as e:
#    print(e)
#finally:
#    if fp is not None:
#        fp.close()

## менеджер контекста
#try:
#    with open('myfile.txt') as fp:
#        for t in fp:
#            print(t)
#except Exception as e:
#    print(e)

# менеджеры контекста можно вкладывать друг в друга
try:
    with open('myfile.txt') as fin:
        with open('out.txt', 'w') as fout:
            for line in fin:
                fout.write(line)
except Exception as e:
    print(e)


# сложение векторов
class DefenerVertor:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # делаем копию вектора v
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        # если не было исключений
        if exc_type is None:
            # новое значение из копии присваиваем основному вектору
            self.__v[:] = self.__temp
        # для перехода на уровень выше и вывода текста ошибки
        # Если не писать то по умолчанию False
        # True - игнорирует ошибку и не склвдывает
        #return False


v1 = [1, 2, 3]
v2 = [1, 2]
try:
    with DefenerVertor(v1) as dv:
        for i in range(len(dv)):
            dv[i] += v2[i]
except Exception as e:
    print(e)

print(v1)