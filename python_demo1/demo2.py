import datetime

from python_demo1 import demo1

print(demo1.my_name)
print(type(demo1.my_name))

result=demo1.add(10,11.2)
print(result)

print(type(result))

num1=20
print("hello "+str(num1)+"kjjj")
print(f"hello {demo1.my_name}")

print(datetime.date.today().strftime("%m/%d/%Y"))