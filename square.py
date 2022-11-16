from rectangle import *

class Square(Rectangle):

    def __repr__(self):
        data = super().get_data()
        self.__width = data[1]
        self.__color = data[2]
        self.__area = self.__width ** 2
        return "\
========================\n\
Квадрат:\n\
Сторона: {}\n\
Цвет: {}\n\
Площадь: {}\n\
========================".format(self.__width, self.__color, self.__area)
