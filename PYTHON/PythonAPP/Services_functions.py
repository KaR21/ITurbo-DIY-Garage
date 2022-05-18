import pickle
import Basic_Metods
import Service

def menuservices():
    menuSEROption = -1
    print("For the management system of the services what file do you want to use?")
    fileName = Basic_Metods.BasicMethods.askForFile()
    while (menuSEROption != 0):
        print("\n------------------------MENU SERVICES------------------------")
        print("1) Update a service")
        print("2) Delete a service")
        print("3) Insert new service and save on a file")
        print("4) See all the services")
        print("0) Exit")
        print("--------------------------------------------------------------\n")
        menuSEROption = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")
        if menuSEROption == 1: #Update a service
            updateAservice(fileName)
        elif menuSEROption == 2: #Delete a service
            deleteAservice(fileName)
        elif menuSEROption == 3: #Insert new service  #Save the services on a file 
            saveAndCreateTheservices(fileName)
        elif menuSEROption == 4: #See all the services
            seeAllTheservices(fileName)

def createANewservice():
    print("\n---------------------------------------------------------------------")
    print("---------------- You are going to CREATE a service.-----------------")
    print("---------------------------------------------------------------------\n")
    id = Basic_Metods.BasicMethods.askAString("Enter the id: \n")
    name = Basic_Metods.BasicMethods.askAString("Enter service´s name: \n")
    empID = Basic_Metods.BasicMethods.askAString("Enter the employee id: \n")
    cabinID = Basic_Metods.BasicMethods.askAnInt("Enter the cabin id: \n")
    
    service = Service.Service(id, name, empID, cabinID)
    return service

def seeAllTheservices(fileName):
    print("\n---------------------------------------------------------------------")
    print("--------------- You are going to SEE all the services.--------------")
    print("---------------------------------------------------------------------\n")
    Basic_Metods.BasicMethods.readFile(fileName)
        
    
def saveAndCreateTheservices(fileName):
    ans = 1
    while ans == 1:
        c1 = createANewservice()
        print("\n---------------------------------------------------------------------")
        print("---------------------- SAVING the service... -----------------------")
        print("---------------------------------------------------------------------\n")
        Basic_Metods.BasicMethods.save_objectOn_File(c1,fileName)
        ans = Basic_Metods.BasicMethods.askAnInt("Do you want to add a new service? (1/0)")
    del c1

def deleteAservice(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- DELETING the service --------------------------")
    print("---------------------------------------------------------------------\n")
    services = []
    seeAllTheservices(fileName)
    print("Which service you want to delete?")
    id = Basic_Metods.BasicMethods.askAString("Enter the id of the service:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, id)
    if pos != -1:
        services = Basic_Metods.BasicMethods.readFileToList(fileName)
        services.pop(pos)
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, services)
    else:
        print("The service does not exist.")
   

def updateAservice(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- UPDATING the service --------------------------")
    print("---------------------------------------------------------------------\n")
    services = []
    seeAllTheservices(fileName)
    print("Which service you want to update?")
    id = Basic_Metods.BasicMethods.askAString("Enter the id of the service:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, id)
    if pos != -1:
        services = Basic_Metods.BasicMethods.readFileToList(fileName)
        print("\n-----------------Enter the new information of the service-----------------\n")
        
        print("Do you want to change the id? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            services[pos].setid()
            
        print("Do you want to change the name? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            services[pos].setname()
            
        print("Do you want to change the employee id? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            services[pos].setempID()
            
        print("Do you want to change the cabin id? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            services[pos].setcabinID()
            
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, services)
    else:
        print("The service does not exist.")
