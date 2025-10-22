#Magic methods are the functions inside or outside the class with double underscore

# suppose we have a vector class and we have to add the 2 vector objects

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print(self.x + other.x , self.y + other.y)

    def show(self,other):
        print(f'x:{self.x},y: {self.y}')
        print(f'x:{other.x},y: {other.y}')

v1 = vector(10,20)
v2 = vector(20,30)

v1.__add__(v2)          #30 50

v1.show(v2)           #x:10,y: 20 x:20,y: 30