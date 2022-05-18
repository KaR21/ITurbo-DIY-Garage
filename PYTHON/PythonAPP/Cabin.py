import Basic_Metods

class Cabin:
    def __init__(self, id, d, h, a, n):

        self.id = id
        self.dim = d
        self.height = h
        self.available = a
        self.name = n
        

    def setid(self):
        self.id = Basic_Metods.BasicMethods.askAString("Enter the new id:\n")

    def setdim(self):
        self.dim = Basic_Metods.BasicMethods.askAnInt("Enter the new dimension:\n")

    def setheight(self):
        self.dim = Basic_Metods.BasicMethods.askAnInt("Enter the new height:\n")
    
    def setavailable(self):
        self.available = Basic_Metods.BasicMethods.askAString("Enter the new available:\n")
    
    def setname(self):
        self.name = Basic_Metods.BasicMethods.askAString("Enter the new name:\n")
    
    def getid(self):
        return self.id

    def getdim(self):
        return self.dim
    
    def getheight(self):
        return self.height
    
    def getavailable(self):
        return self.available
    
    def getname(self):
        return self.name


    def toString(self):
        print(self.id, self.dim, self.height, self.available, self.name)
        