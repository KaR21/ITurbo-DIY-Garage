import Basic_Metods

class Person:
    def __init__(self, i,n, s, mp, hp, r, e, p, c):

        self.id = i
        self.name = n
        self.surname = s
        self.mobile_phone = mp
        self.home_phone = hp
        self.role = r
        self.email = e
        self.password = p
        self.condition = c


    def setid(self):
        self.id = Basic_Metods.BasicMethods.askAString("Enter the id: ")

    def setname(self):
        self.name = Basic_Metods.BasicMethods.askAString("Enter the name: ")

    def setsurname(self):
        self.surname = Basic_Metods.BasicMethods.askAString("Enter the last name: ")

    def setmobilePhone(self):
        self.mobile_phone = Basic_Metods.BasicMethods.askAnInt("Enter the mobile phone number: ")

    def sethomePhone(self):
        self.home_phone = Basic_Metods.BasicMethods.askAnInt("Enter the home phone number: ")

    def setrole(self):
        self.role = Basic_Metods.BasicMethods.askAString("Enter the role: ")

    def setemail(self):
        self.email = Basic_Metods.BasicMethods.askAString("Enter the email: ")

    def setpassword(self):
        self.password = Basic_Metods.BasicMethods.askAString("Enter the password: ")

    def setaddress(self):
        self.address = Basic_Metods.BasicMethods.askAString("Enter the address: ")
        
    def setcity(self):
        self.city = Basic_Metods.BasicMethods.askAString("Enter the city: ")

    def setpostcode(self):
        self.postcode = Basic_Metods.BasicMethods.askAnInt("Enter the postcode: ")
        
    def setcondition(self):
        self.condition = Basic_Metods.BasicMethods.askAString("Enter the condition: ")
    



    def getid(self):
        return self.id

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
        print(self.id, self.name, self.surname, self.mobile_phone, self.home_phone, self.role, self.email, self.password)
        