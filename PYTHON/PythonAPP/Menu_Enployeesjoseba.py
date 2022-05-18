import Basic_Metods
import Enployees
import Person
import pickle

def menuEnployees():
    option = -1
    print("For the management system of the employees what file do you want to use?")
    filename = Basic_Metods.BasicMethods.askForFile()

    while (option !=0):
        print("\n------------------------MENU EMPLOYEES------------------------")
        print("1) Create a new enployee")
        print("2) Update an enployee")
        print("3) Delete an enployee")
        print("4) See all the enployees")
        print("0) Exit")
        print("--------------------------------------------------------------\n")
        option = Basic_Metods.BasicMethods.askInteger("Enter your option: ")
        if option == 1:
            add_enployee(filename)

        elif option == 2:
            update_enployee(filename)

        elif option == 3:
            delete_enployee(filename)

        elif option == 4:
            show_all_enployees(filename)

def createANewEmployee():
    print("\n---------------------------------------------------------------------")
    print("---------------- You are going to CREATE a employee.-------------------")
    print("---------------------------------------------------------------------\n")
    dni = Basic_Metods.BasicMethods.askAString("Enter the DNI: \n")
    name = Basic_Metods.BasicMethods.askAString("Enter employee´s name: \n")
    surname = Basic_Metods.BasicMethods.askAString("Enter employee´s last name: \n")
    home_phone = Basic_Metods.BasicMethods.askAnInt("Enter employee´s home phone number: \n")
    mobile_phone = Basic_Metods.BasicMethods.askAnInt("Enter employee´s mobile phone number: \n")
    email = Basic_Metods.BasicMethods.askAString("Enter employee´s email: \n")
    password = Basic_Metods.BasicMethods.askAString("Enter employee´s password: \n")
    address = Basic_Metods.BasicMethods.askAString("Enter employee´s address: \n")
    city = Basic_Metods.BasicMethods.askAString("Enter employee´s city: \n")
    postcode = Basic_Metods.BasicMethods.askAnInt("Enter employee´s postcode: \n")
    role = Basic_Metods.BasicMethods.askAString("Enter employee´s role: \n")
    condition = Basic_Metods.BasicMethods.askAString("Enter employee´s condition: \n")
    salary = Basic_Metods.BasicMethods.askAnDouble("Enter employee´s salary: \n")

    person = Person.Person(dni, name, surname, home_phone, mobile_phone, email, password, address, city, postcode, role, condition)
    employee = Enployees.Enployees(person, salary)
    return employee
    

def add_enployee(fileName):
    ans = 1
    while ans == 1:
        emp = createANewEmployee()
        print("\n---------------------------------------------------------------------")
        print("---------------------- SAVING the employee... -----------------------")
        print("---------------------------------------------------------------------\n")
        Basic_Metods.BasicMethods.save_objectOn_File(emp,fileName)
        ans = Basic_Metods.BasicMethods.askAnInt("Do you want to add a new employee? (1/0)")
    del emp

def show_all_enployees(fileName):
    print("\n---------------------------------------------------------------------")
    print("--------------- You are going to SEE all the employees.----------------")
    print("---------------------------------------------------------------------\n")
    Basic_Metods.BasicMethods.readFile(fileName)


def update_enployee(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- UPDATING the customer --------------------------")
    print("---------------------------------------------------------------------\n")
    employees = []
    show_all_enployees(fileName)
    print("Which employee you want to update?")
    dni = Basic_Metods.BasicMethods.askAString("Enter the DNI of the employee:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, dni)
    if pos != -1:
        employees = Basic_Metods.BasicMethods.readFileToList(fileName)
        print("\n-----------------Enter the new information of the employee-----------------\n")
        
        print("Do you want to change the DNI? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setid()
            
        print("Do you want to change the name? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setname()
            
        print("Do you want to change the surname? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setsurname()
            
        print("Do you want to change the mobile phone? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setmobilePhone()
            
        print("Do you want to change the home phone? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].sethomePhone()
        
        print("Do you want to change the email? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setemail() 
            
        print("Do you want to change the password? (1/0)") 
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setpassword()
            
        print("Do you want to change the address? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setaddress()
            
        print("Do you want to change the city? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setcity()
        
        print("Do you want to change the postcode? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setpostcode()
        
        print("Do you want to change the role? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setrole()
        
        print("Do you want to change the condition? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            employees[pos].setcondition()
        
        print("Do you want to change the salary? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnDouble("Enter an option: \n")
        if answer == 1:
            employees[pos].setSalary()
            
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, employees)
    else:
        print("The employee does not exist.")

def delete_enployee(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- DELETING the customer --------------------------")
    print("---------------------------------------------------------------------\n")
    employees = []
    show_all_enployees(fileName)
    print("Which employees you want to delete?")
    dni = Basic_Metods.BasicMethods.askAString("Enter the DNI of the employees:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, dni)
    if pos != -1:
        employees = Basic_Metods.BasicMethods.readFileToList(fileName)
        employees.pop(pos)
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, employees)
    else:
        print("The employees does not exist.")