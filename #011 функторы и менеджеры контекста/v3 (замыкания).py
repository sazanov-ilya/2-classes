#class StripChars:
#    def __init__(self, chars):
#        self.__chars = chars
#
#    def __call__(self, *args, **kwargs):
#        if not isinstance(args[0], str):
#            raise ValueError('Аргумент должен быть строкой')
#
#        return  args[0].strip(self.__chars)

def StripChars(chars):
    def stringStrip(string):
        if not isinstance(string, str):
            raise ValueError('Аргумент должен быть строкой')
        return string.strip(chars)
    return stringStrip

s1 = StripChars('?:!.; ')
print( s1(' Hello world! ') )

# это 2 разных объекта
s2 = StripChars('?:.; ')
print( s2(' Hello! ') )

print( id(s1), id(s2), sep='\n')