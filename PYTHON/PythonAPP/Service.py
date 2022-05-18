import Basic_Metods

class Service:
    def __init__(self, id, n,empID, cabinID):

        self.id = id
        self.name = n
        self.empid = empID
        self.cabinid = cabinID
        

    def setid(self):
        self.id = Basic_Metods.BasicMethods.askAString("Enter the new id:\n")

    def setname(self):
        self.name = Basic_Metods.BasicMethods.askAString("Enter the new name:\n")

    def setsurname(self):
        self.empid = Basic_Metods.BasicMethods.askAString("Enter the new employee id:\n")

    def setmobilePhone(self):
        self.cabinid = Basic_Metods.BasicMethods.askAnInt("Enter the new cabin id:\n")

    
    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def getsurname(self):
        return self.empid

    def getmobilePhone(self):
        return self.cabinid


    def toString(self):
        print(self.id, self.name, self.empid, self.cabinid)
        