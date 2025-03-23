
import math

class Circle:

    def __init__(self, radius):

        self.radius = radius

    def perimeter(self):

        return 2 * math.pi * self.radius
    
    def area(self):

        return math.pi * self.radius ** 2 
    
    def operation_circle(self, operation_str):

        if operation_str == 'perimeter':

            result = self.perimeter()
            printed_result = f'{result:.2f}'
        
        elif operation_str == 'area':
            
            result = self.area()
            printed_result = f'{result:.2f}'

        return printed_result
