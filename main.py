from color import *
from rectangle import *
from circle import *
from square import *


def main():
    figure1 = Rectangle(Color("11","22","31"), 10, 20)
    print(figure1)
    figure2 = Circle(8, Color("12","34","96"))
    print(figure2)
    figure3 = Square(Color("25", "67", "58"), 10)
    print(figure3)

if __name__ == '__main__':
    main()
