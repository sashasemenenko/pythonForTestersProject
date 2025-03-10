class Shape:
    def __init__(self, name: str):
        self.name = name


class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: int, height: int):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return self.base * 0.5 * self.height

my_circle = Circle(5)
print(my_circle.name)
print(my_circle.radius)
print(f"The area of the {my_circle.name} is {my_circle.area()}.")

my_rectangle = Rectangle(4, 5)
print(my_rectangle.name)
print(my_rectangle.height)
print(my_rectangle.width)
print(f"The area of the {my_rectangle.name} is {my_rectangle.area()}.")

my_triange = Triangle(4, 5)
print(my_triange.name)
print(my_triange.base)
print(my_triange.height)
print(f"The area of the {my_triange.name} is {my_triange.area()}.")