import BasicMethod
class Manager:

    def __init__(self,si,sn,ss):
        self.Id=si
        self.name=sn
        self.surname=ss

    def setId(self):
        self.Id= BasicMethod.BasicMethods.askInterger("Id")

    def setname(self):
        self.name = BasicMethod.BasicMethods.askString("name")

    def setsurname(self):
        self.surname = BasicMethod.BasicMethods.askString("surname")

    def print(self):
        print(self.Id,self.name,self.surname)

