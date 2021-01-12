class Point:
    default_color = 'red'  # this is a class level attribute

    # all def methods in a class have a self as the first variable.
    def __init__(self, x, y):
        self.x = x  # these are attributes
        self.y = y

    def draw(self):
        print(f'Point ({self.x}, {self.y})')

    @classmethod  # this is a decorator. is necessary for making a class method
    def zero(cls):
        return cls(0, 0)


point = Point(1, 2)
another = Point(3, 4)

point.z = 10
point.draw()

print(point.default_color, another.default_color)
Point.default_color = 'yellow'  # this line changes the default color inside the class definition!
print(point.default_color, another.default_color)

## class method:
point = Point.zero()
point.draw()
print(
    point.__str__())  # this is a magic method. they are predefined,
# but we can reassign them to be more accurate inside the class definition
