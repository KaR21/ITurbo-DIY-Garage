import Basic_Metods

class Products:
    def __init__(self, id, g, n, d, p, a, av, s):

        self.id = id
        self.group = g
        self.name = n
        self.description = d
        self.price = p
        self.amount = a
        self.available = av
        self.supplier = s
        
        

    def setid(self):
        self.id = Basic_Metods.BasicMethods.askAString("Enter the new id:\n")
    
    def setgroup(self):
        self.group = Basic_Metods.BasicMethods.askAString("Enter the new group:\n")
    
    def setname(self):
        self.name = Basic_Metods.BasicMethods.askAString("Enter the new name:\n")
    
    def setdescription(self):
        self.description = Basic_Metods.BasicMethods.askAString("Enter the new description:\n")
    
    def setprice(self):
        self.price = Basic_Metods.BasicMethods.askAnDouble("Enter the new price:\n")
    
    def setamount(self):
        self.amount = Basic_Metods.BasicMethods.askAnInt("Enter the new amount:\n")
    
    def setavailable(self):
        self.available = Basic_Metods.BasicMethods.askAString("Enter the new available:\n")
    
    def setsupplier(self):
        self.supplier = Basic_Metods.BasicMethods.askAString("Enter the new supplier:\n")
    
    def getsupplier(self):
        return self.supplier
    
    def getid(self):
        return self.id
    
    def getname(self):
        return self.name
    
    def getprice(self):
        return self.price
    
    def getamount(self):
        return self.amount
    
    def getgroup(self):
        return self.group
    
    def getdescription(self):
        return self.description


    def toString(self):
        print(self.id, self.group, self.name, self.description, self.price, self.amount, self.available, self.supplier)
        