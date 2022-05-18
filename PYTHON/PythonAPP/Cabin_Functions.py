import pickle
import Basic_Metods
import Cabin

def menucabins():
    menuCABINOption = -1
    print("For the management system of the cabins what file do you want to use?")
    fileName = Basic_Metods.BasicMethods.askForFile()
    while (menuCABINOption != 0):
        print("\n------------------------MENU CABINS------------------------")
        print("1) Update a cabin")
        print("2) Delete a cabin")
        print("3) Create a new cabin and save on a file")
        print("4) See all the cabins")
        print("0) Exit")
        print("--------------------------------------------------------------\n")
        menuCABINOption = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")
        if menuCABINOption == 1: #Update a cabin
            updateAcabin(fileName)
        elif menuCABINOption == 2: #Delete a cabin
            deleteAcabin(fileName)
        elif menuCABINOption == 3: #InCABINt new cabin  #Save the cabins on a file 
            saveAndCreateThecabins(fileName)
        elif menuCABINOption == 4: #See all the cabins
            seeAllThecabins(fileName)

def createANewcabin():
    print("\n---------------------------------------------------------------------")
    print("---------------- You are going to CREATE a cabin.-----------------")
    print("---------------------------------------------------------------------\n")
    id = Basic_Metods.BasicMethods.askAString("Enter the id: \n")
    dim = Basic_Metods.BasicMethods.askAnInt("Enter the dimension: \n")
    height = Basic_Metods.BasicMethods.askAnInt("Enter the height: \n")
    avalaible = Basic_Metods.BasicMethods.askAString("Enter the avalaible: \n")
    name = Basic_Metods.BasicMethods.askAString("Enter cabin´s name: \n")
    
    cabin = Cabin.Cabin(id, dim, height, avalaible, name)
    return cabin

def seeAllThecabins(fileName):
    print("\n---------------------------------------------------------------------")
    print("--------------- You are going to SEE all the cabins.-------------------")
    print("---------------------------------------------------------------------\n")
    Basic_Metods.BasicMethods.readFile(fileName)
        
    
def saveAndCreateThecabins(fileName):
    ans = 1
    while ans == 1:
        c1 = createANewcabin()
        print("\n---------------------------------------------------------------------")
        print("---------------------- SAVING the cabin... ----------------------------")
        print("---------------------------------------------------------------------\n")
        Basic_Metods.BasicMethods.save_objectOn_File(c1,fileName)
        ans = Basic_Metods.BasicMethods.askAnInt("Do you want to add a new cabin? (1/0)")
    del c1

def deleteAcabin(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- DELETING the cabin --------------------------")
    print("---------------------------------------------------------------------\n")
    cabins = []
    seeAllThecabins(fileName)
    print("Which cabin you want to delete?")
    id = Basic_Metods.BasicMethods.askAString("Enter the id of the cabin:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, id)
    if pos != -1:
        cabins = Basic_Metods.BasicMethods.readFileToList(fileName)
        cabins.pop(pos)
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, cabins)
    else:
        print("The cabin does not exist.")
   

def updateAcabin(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- UPDATING the cabin --------------------------")
    print("---------------------------------------------------------------------\n")
    cabins = []
    seeAllThecabins(fileName)
    print("Which cabin you want to update?")
    id = Basic_Metods.BasicMethods.askAString("Enter the id of the cabin:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, id)
    if pos != -1:
        cabins = Basic_Metods.BasicMethods.readFileToList(fileName)
        print("\n-----------------Enter the new information of the cabin-----------------\n")
        
        print("Do you want to change the id? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            cabins[pos].setid()
        
        print("Do you want to change the dimension? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            cabins[pos].setdim()
        
        print("Do you want to change the height? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            cabins[pos].setheight()
        
        print("Do you want to change the avalaible? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            cabins[pos].setavalaible()
            
        print("Do you want to change the name? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            cabins[pos].setname()
            
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, cabins)
    else:
        print("The cabin does not exist.")
