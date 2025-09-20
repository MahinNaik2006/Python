class Empl:
    def __init__(self, name, id):
     self.name = name
     self.id = id

    def show_details(self):
        print(f"The name of the id {self.id} is {self.name}")

class Em(Empl):
    def salr(self,sal):
        self.sal = sal
        print(f"The salary is {self.sal}")

e1 = Em("Mahin" , 2300)
e1.show_details()
e1.salr("20000$")