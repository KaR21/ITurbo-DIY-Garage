import Basic_Metods

def menuCustomers():
    menuCUSOption = -1
    customers = []
    while (menuCUSOption != 0):
        print("------------------------MENU CUSTOMERS------------------------")
        print("1) Update a customer")
        print("2) Delete a customer")
        print("3) Insert new customer")
        print("4) See all the customers")
        print("5) Save the customers on a file")
        print("0) Exit")
        print("--------------------------------------------------------------")
        menuCUSOption = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")

        #if menuCUSOption == 1: #Update a customer
        #elif menuCUSOption == 2: #Delete a customer
        if menuCUSOption == 3: #Insert new customer
            createANewCustomer(customers)
        #elif menuCUSOption == 4: #See all the customers
        #elif menuCUSOption == 5: #Save the customers on a file


def printCustomer(self):
    print(self.id, self.name, self.surname, self.phone_home, self.phone_mobile, self.email, self.address, self.city, self.postcode)


def createANewCustomer(customers):
    print("---------------------------------------------------------------------")
    print("------- You are going to CREATE a new customer. Are you sure? -------")
    print("---------------------------------------------------------------------")
    sure = Basic_Metods.BasicMethods.askAString("Enter yes or no: ")
    print(sure)
    print(sure.capitalize)
    if sure.upper == "YES":
        dni = False
        while not dni: #the same as dni == False
            dniNumber = Basic_Metods.BasicMethods.askAnInt("Enter the DNI number")
            dniLetter = Basic_Metods.BasicMethods.askAString("Enter the DNI letter")
            dni = Basic_Metods.BasicMethods.validateDNI(dniNumber, dniLetter)
        dniAll = [dniNumber, dniLetter]

        name = Basic_Metods.BasicMethods.askAString("Enter customer´s name")

        surname = Basic_Metods.BasicMethods.askAString("Enter customer´s last name")

        home_phone = Basic_Metods.BasicMethods.askAnInt("Enter customer´s home phone number")

        mobile_phone = Basic_Metods.BasicMethods.askAnInt("Enter customer´s mobile phone number")

        email = Basic_Metods.BasicMethods.askAString("Enter customer´s email")

        password = Basic_Metods.BasicMethods.askAString("Enter customer´s password")

        address = Basic_Metods.BasicMethods.askAString("Enter customer´s address")

        city = Basic_Metods.BasicMethods.askAString("Enter customer´s city")

        postcode = Basic_Metods.BasicMethods.askAnInt("Enter customer´s postcode")

        role = Basic_Metods.BasicMethods.askAString("Enter customer´s role")

        condition = Basic_Metods.BasicMethods.askAString("Enter customer´s condition")

        customer = [dniAll, name, surname, home_phone, mobile_phone, email, password, address, city, postcode, role,
                    condition]

        customers.add(customer)
    return customers
