import Basic_Metods

class Booking:
    def __init__(self, id,d, hourIn, hourOut, cus, c, p): #Constructor

        self.id = id
        self.date = d
        self.hourIn = hourIn
        self.hourOut = hourOut
        self.customerID = cus
        self.cabinID = c
        self.price = p

    def setid(self):
        self.id = Basic_Metods.BasicMethods.askAString("Enter the new id:\n")

    def setdate(self):
        self.date = Basic_Metods.BasicMethods.askAString("Enter the new date:\n")

    def sethourIn(self):
        self.hourIn = Basic_Metods.BasicMethods.askAString("Enter the new hourIn:\n")
        
    def sethourOut(self):
        self.hourOut = Basic_Metods.BasicMethods.askAString("Enter the new hourOut:\n")

    def setcusID(self):
        self.customerID = Basic_Metods.BasicMethods.askAString("Enter the new customer ID:\n")

    def setcabinID(self):
        self.cabinID = Basic_Metods.BasicMethods.askAnInt("Enter the new cabinID:\n")

    def setprice(self):
        self.price = Basic_Metods.BasicMethods.askAnDouble("Enter the new price:\n")


    def getid(self):
        return self.id
        
    def getdate(self):
        return self.date

    def gethourIn(self):
        return self.hourIn

    def gethourOut(self):
        return self.hourOut

    def getcusID(self):
        return self.cusID

    def getcabinID(self):
        return self.cabinID

    def getprice(self):
        return self.price

    def toString(self):
        print(self.id, self.date, self.hourIn, self.hourOut, self.customerID, self.cabinID, self.price)
       
