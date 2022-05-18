import Basic_Metods

class Person:
    def __init__(self, i,n, s, mp, hp, e, passw, a, c, p, r, cond):

        self.dni = i
        self.name = n
        self.surname = s
        self.mobile_phone = mp
        self.home_phone = hp
        self.email = e
        self.password = passw
        self.address = a
        self.city = c
        self.postcode = p
        self.role = r
        self.condition = cond

    def setid(self):
        self.dni = Basic_Metods.BasicMethods.askAString("Enter the new id:\n")

    def setname(self):
        self.name = Basic_Metods.BasicMethods.askAString("Enter the new name:\n")

    def setsurname(self):
        self.surname = Basic_Metods.BasicMethods.askAString("Enter the new last name:\n")

    def setmobilePhone(self):
        self.mobile_phone = Basic_Metods.BasicMethods.askAnInt("Enter the new mobile phone number:\n")

    def sethomePhone(self):
        self.home_phone = Basic_Metods.BasicMethods.askAnInt("Enter the new home phone number:\n")

    def setrole(self):
        self.role = Basic_Metods.BasicMethods.askAString("Enter the new role:\n")

    def setemail(self):
        self.email = Basic_Metods.BasicMethods.askAString("Enter the new email:\n")

    def setpassword(self):
        self.password = Basic_Metods.BasicMethods.askAString("Enter the new password:\n")

    def setaddress(self):
        self.address = Basic_Metods.BasicMethods.askAString("Enter the new address:\n")
        
    def setcity(self):
        self.city = Basic_Metods.BasicMethods.askAString("Enter the new city:\n")

    def setpostcode(self):
        self.postcode = Basic_Metods.BasicMethods.askAnInt("Enter the new postcode:\n")
        
    def setcondition(self):
        self.condition = Basic_Metods.BasicMethods.askAString("Enter the new condition:\n")
    



    def getid(self):
        return self.dni

    def getname(self):
        return self.name

    def getsurname(self):
        return self.surname

    def getmobilePhone(self):
        return self.mobile_phone

    def gethomePhone(self):
        return self.home_phone

    def getrole(self):
        return self.role

    def getemail(self):
        return self.email

    def getpassword(self):
        return self.password

    def getaddress(self):
        return self.address
        
    def getcity(self):
        return self.city

    def getpostcode(self):
        return self.postcode
        
    def getcondition(self):
        return self.condition



    def toString(self):
        print(self.dni, self.name, self.surname, self.mobile_phone, self.home_phone, self.email, self.password, self.address, self.city, self.postcode, self.role, self.condition)
        