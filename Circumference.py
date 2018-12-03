#Chris Jones
#ISAT 252
#Final Exam Part V
#Python 3.6.2

import math

class Circle:
 
    def __init__(self,radius):
        self.__radius=radius
        
    def get_radius(self):
        return self.__radius
    
    def set_radius(self,new_radius):
        self.__radius=new_radius
        
    def area(self):
        return math.pi*self.__radius**2
    
    def circumference(self):
        return 2*math.pi*self.__radius
    
def main():
    try:
        radius=int(input("Please enter the radius of the circle in inches: "))
        my_circle=Circle(radius)
        my_circle.area()
        print("The area of the circle is", format(my_circle.area(),".2f"),"inches squared.")
        my_circle.circumference()
        print("The circumference of the circle is", format(my_circle.circumference(),".2f"),"inches.")
    
    except:
        print("Please enter a numerical value.")
        
        
        
main()
