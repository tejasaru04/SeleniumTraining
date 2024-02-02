import math


def area_of_circle(radius):
    return math.pi*radius*radius

class Area:
    def area_of_square(self,side):
        return side*side

class Volume:
    def __init__(self):
        print(50*"-")
        print("Object created")
        print("chrome browser launch")
        print("-------------------------")

    def volume_of_cube(self,edge):
        return math.pow(edge,3)

    @staticmethod
    def print_author():
        print("Balaji Dinakaran")

    @property
    def author_name(self):
        return "Balaji Dinakaran"

    @property
    def get_area_instance(self):
        a=Area()
        return a