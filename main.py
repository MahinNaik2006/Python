class person:

    def __init__(self , age , Name):
        self.age = age
        self.Name = Name

    def out(self):
        print(f'Person Name is {self.Name} and age is {self.age}')


g1 = person(18 , "Mahin")
g1.out()