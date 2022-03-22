from Manager import Manager
class Enployees(Manager):
    def __init__(self,si,sn,ss,sa,sm,se,sd):
        super().__init__(si,sn,ss)
        self.adress = sa
        self.movile = sm
        self.email = se
        self.dpto = sd

    def setadress(self):
        self.adress = input("Enter adress")

    def setmovile(self):
        self.movile = input("Enter movile number")

    def setemail(self):
        self.email = input("Enter email")

    def setdpto(self):
        self.dpto = input("Enter dpto")

    def print(self):
        print(self.Id,self.name,self.surname,self.adress,self.movile,self.email,self.dpto)
