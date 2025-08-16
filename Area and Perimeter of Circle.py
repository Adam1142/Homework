import math
class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
       return math.pi * (self.radius ** 2)
    def perimeter(self):
       return 2 * math.pi * self.radius
x = float(input("Enter the value of the radius: "))
ob = circle(x)
print(f"Area of circle: {ob.area():.2f}")
print(f"Perimeter of circle: {ob.perimeter():.2f}")