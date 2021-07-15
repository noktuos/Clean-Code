# Desafio de la seccion 1 de Clean Code
#Codigo original
#Lenguaje Python

class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, starting_point, broad, high):
        self.starting_point = starting_point
        self.broad = broad
        self.high = high

    def area(self):
        return self.broad * self.high

    def end_points(self):
        top_right = self.starting_point.coordX + self.broad
        bottom_left = self.starting_point.coordY + self.high
        print('Starting Point (X)): ' + str(self.starting_point.coordX))
        print('Starting Point (Y)): ' + str(self.starting_point.coordY))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_stuff():
    main_point = Point(50, 100)
    rect = Rectangle(main_point, 90, 10)

    return rect


my_rect = build_stuff()

print(my_rect.area())
my_rect.end_points()


######################################################################################
# Desafio de la seccion 1 de Clean Code (Solucionado)
#Codigo personal
#Lenguaje Python

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


class Rectangle:
    def __init__(self, starting_point, width, height):
        self.starting_point = starting_point
        self.width = width
        self.heigth = height

    def calculate_area(self):
        return self.width * self.heigth

    def end_points(self):
        top_right = self.starting_point.X + self.width
        bottom_left = self.starting_point.Y + self.heigth
        print('Starting Point (X)): ' + str(self.starting_point.X))
        print('Starting Point (Y)): ' + str(self.starting_point.Y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    starting_point = Point(50, 100)
    rectangle = Rectangle(starting_point, 90, 10)

    return rectangle


my_rectangle = build_rectangle()

print(my_rectangle.calculate_area())
my_rectangle.end_points()

# Que se podria haber hecho mejor
    #getArea en lugar de calculateArea
    #uso de rectangle en lugar de my_rectangle como nombre
    #El metodo end_points puede cambiar de nombre a print_coordinates, aunque tambien podria ser usado el end_points