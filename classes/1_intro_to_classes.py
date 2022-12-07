# "class" is the keyword that classes start with in Python.

class Facade:
    pass

facade_1 = Facade()
facade_1_type = type(facade_1)
# print(facade_1_type)

class Grade:
    minimum_passing = 60

science_class = Grade()
# print(science_class.minimum_passing)

class Rules:
    def washing_brushes(self):
        print("Washing Washy the Brushies.")
        return
    
ninja = Rules()
# print(ninja.washing_brushes())
# print(Rules.washing_brushes) #Shows memory location of class

#Methods with Arguments
import math
# print(math.pi)
class Circle:
    pi = math.pi
    def area(self, radius):
        return self.pi * radius ** 2
circle_1 = Circle()
#Note: A = pi * r^2 
# radius is half the diameter, so a 12 inch pizza has a diameter of 12. to calculate the radius, you divide it by 2. You could have asked for the diameter and created the function to automatically divide the diameter by 2. 
pizza_area = circle_1.area(12/2)
print(pizza_area)
