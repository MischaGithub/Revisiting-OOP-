#Revisiting OOP and classes

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * (self.length + self.width)

print("To find the area and perimeter of a Rectangle...")

length = int(input("Enter length: \n"))
width = int(input("Enter width: \n"))

r_1 = Rectangle(length, width)
print("Area: ", r_1.find_area())
print("Perimeter: ", r_1.find_perimeter())
