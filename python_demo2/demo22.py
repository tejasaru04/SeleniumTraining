#module import
from python_demo1 import demo1

#method import
from python_demo1.demo1 import add

#package import
import python_demo1


print(demo1.my_name)

print(demo1.add(10,33))


print(add(3,3))

print(python_demo1.demo1.sub(2, 3))

print(python_demo1.d1.add(2, 3))

print(python_demo1.area.area_of_circle(5))