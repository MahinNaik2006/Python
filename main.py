# This is Magic method
# suppose we have 2 vectors and you want to add them then you have to use the magic method

# v1 = Vector(10,20)
# v2 = Vector(10,20)
# we can not just start add these 2 vector so we have these magic methods

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("add method is called")
        print(f'{self.x + other.x},{self.y+other.y}')

v1 = Vector(20,40)
v2 = Vector(30,90)

v1.__add__(v2)
