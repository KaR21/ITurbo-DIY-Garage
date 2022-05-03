import Basic_Metods
from Customer_Functions import *

menuOption = -1
print("----------------------------------------------------")
print("                 WELCOME TO ITURBO!!")
print("----------------------------------------------------")
print("\n\n")

while menuOption != 0:
    print("------------------------MENU------------------------")
    print("1) Manage enployees") #An option related with the management system of the employees
    print("2) Manage customers") #An option related with the management system of the customers
    print("3) Manage bookings") #An option related with the management system of the bookings
    print("4) Manage cabins") #An option related with the management system of the cabins
    print("5) See facturation") #An option to see all the facturation achieve between a time gap
    print("6) See the best customer") #An option related with the best customer (who has booked/bought more)
    print("0) EXIT")
    print("----------------------------------------------------")
    menuOption = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")

    if menuOption == 1:
        print("------------------------MENU EMPLOYEES------------------------")
        print("--------------------------------------------------------------")
    elif menuOption == 2:
        menuCustomers()

    elif menuOption == 3:
        print("-------------------------MENU BOOKINGS------------------------")
        print("--------------------------------------------------------------")

    elif menuOption == 4:
        print("-------------------------MENU CABINS--------------------------")
        print("--------------------------------------------------------------")

    #elif menuOption == 5:

    #elif menuOption == 6:

    #elif menuOption == 9:

    elif menuOption == 0:
        print("Goodbye!")
        input("Press enter to close...")
    else:
        print("invalid number")

