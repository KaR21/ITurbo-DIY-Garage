import pickle
import Basic_Metods
import Person

def menuCustomers():
    menuCUSOption = -1
    print("For the management system of the customers what file do you want to use?")
    fileName = Basic_Metods.BasicMethods.askForFile()
    while (menuCUSOption != 0):
        print("\n------------------------MENU CUSTOMERS------------------------")
        print("1) Update a customer")
        print("2) Delete a customer")
        print("3) Insert new customer and save on a file")
        print("4) See all the customers")
        print("0) Exit")
        print("--------------------------------------------------------------\n")
        menuCUSOption = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")
        if menuCUSOption == 1: #Update a customer
            updateACustomer(fileName)
        elif menuCUSOption == 2: #Delete a customer
            deleteACustomer(fileName)
        elif menuCUSOption == 3: #Insert new customer  #Save the customers on a file 
            saveAndCreateTheCustomers(fileName)
        elif menuCUSOption == 4: #See all the customers
            seeAllTheCustomers(fileName)

def createANewCustomer():
    print("\n---------------------------------------------------------------------")
    print("---------------- You are going to CREATE a customer.-----------------")
    print("---------------------------------------------------------------------\n")
    dni = Basic_Metods.BasicMethods.askAString("Enter the DNI: \n")
    name = Basic_Metods.BasicMethods.askAString("Enter customer´s name: \n")
    surname = Basic_Metods.BasicMethods.askAString("Enter customer´s last name: \n")
    home_phone = Basic_Metods.BasicMethods.askAnInt("Enter customer´s home phone number: \n")
    mobile_phone = Basic_Metods.BasicMethods.askAnInt("Enter customer´s mobile phone number: \n")
    email = Basic_Metods.BasicMethods.askAString("Enter customer´s email: \n")
    password = Basic_Metods.BasicMethods.askAString("Enter customer´s password: \n")
    address = Basic_Metods.BasicMethods.askAString("Enter customer´s address: \n")
    city = Basic_Metods.BasicMethods.askAString("Enter customer´s city: \n")
    postcode = Basic_Metods.BasicMethods.askAnInt("Enter customer´s postcode: \n")
    role = Basic_Metods.BasicMethods.askAString("Enter customer´s role: \n")
    condition = Basic_Metods.BasicMethods.askAString("Enter customer´s condition: \n")

    customer = Person.Person(dni, name, surname, home_phone, mobile_phone, email, password, address, city, postcode, role, condition)
    return customer

def seeAllTheCustomers(fileName):
    print("\n---------------------------------------------------------------------")
    print("--------------- You are going to SEE all the customers.--------------")
    print("---------------------------------------------------------------------\n")
    Basic_Metods.BasicMethods.readFile(fileName)
        
    
def saveAndCreateTheCustomers(fileName):
    ans = 1
    while ans == 1:
        c1 = createANewCustomer()
        print("\n---------------------------------------------------------------------")
        print("---------------------- SAVING the customer... -----------------------")
        print("---------------------------------------------------------------------\n")
        Basic_Metods.BasicMethods.save_objectOn_File(c1,fileName)
        ans = Basic_Metods.BasicMethods.askAnInt("Do you want to add a new customer? (1/0)")
    del c1

def deleteACustomer(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- DELETING the customer --------------------------")
    print("---------------------------------------------------------------------\n")
    customers = []
    seeAllTheCustomers(fileName)
    print("Which customer you want to delete?")
    dni = Basic_Metods.BasicMethods.askAString("Enter the DNI of the customer:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, dni)
    if pos != -1:
        customers = Basic_Metods.BasicMethods.readFileToList(fileName)
        customers.pop(pos)
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, customers)
    else:
        print("The customer does not exist.")
   

def updateACustomer(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- UPDATING the customer --------------------------")
    print("---------------------------------------------------------------------\n")
    customers = []
    seeAllTheCustomers(fileName)
    print("Which customer you want to update?")
    dni = Basic_Metods.BasicMethods.askAString("Enter the DNI of the customer:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, dni)
    if pos != -1:
        customers = Basic_Metods.BasicMethods.readFileToList(fileName)
        print("\n-----------------Enter the new information of the customer-----------------\n")
        
        print("Do you want to change the DNI? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setid()
            
        print("Do you want to change the name? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setname()
            
        print("Do you want to change the surname? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setsurname()
            
        print("Do you want to change the mobile phone? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setmobilePhone()
            
        print("Do you want to change the home phone? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].sethomePhone()
        
        print("Do you want to change the email? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setemail() 
            
        print("Do you want to change the password? (1/0)") 
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setpassword()
            
        print("Do you want to change the address? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setaddress()
            
        print("Do you want to change the city? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setcity()
        
        print("Do you want to change the postcode? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setpostcode()
        
        print("Do you want to change the role? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setrole()
        
        print("Do you want to change the condition? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            customers[pos].setcondition()
            
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, customers)
    else:
        print("The customer does not exist.")
