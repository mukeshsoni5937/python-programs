class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def Calc_area(self):
        return Circle.pi * self.radius ** 2
    def Calc_cir(self):
        return 2 * Circle.pi * self.radius
rad = float(input("Enter the Radius="))
Circle = Circle(rad)
print("Area of Circle=",Circle.Calc_area())
print("Circle of Circle=",Circle.Calc_cir())