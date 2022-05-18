import Basic_Metods 
from BookCabin_Functions import * # Import the functions from BookCabin_Functions.py
from BookService_Functions import * # Import the functions from BookService_Functions.py
from Customer_Functions import * # Import the functions from Customer_Functions.py
from Menu_Enployeesjoseba import * # Import the functions from Menu_Enployeesjoseba.py
from Products_Functions import * # Import the functions from Products_Functions.py
from Services_functions import * # Import the functions from Services_functions.py
from Cabin_Functions import * # Import the functions from Cabin_Functions.py

menuOption = -1
print("----------------------------------------------------")
print("                 WELCOME TO ITURBO!!")
print("----------------------------------------------------")
print("\n\n")

while menuOption != 0:
    print("------------------------MENU------------------------")
    print("1) Manage employees") #An option related with the management system of the employees
    print("2) Manage customers") #An option related with the management system of the customers
    #TODO
    #print("3) Manage bookings") #An option related with the management system of the bookings

    print("4) Manage services") #An option related with the management system of the services
    print("5) Manage cabins") #An option related with the management system of the cabins
    print("6) Manage products") #An option related with the management system of the products (and for making a purchase)
    #print("7) See facturation") #An option to see all the facturation achieve between a time gap
    #print("8) See the best customer") #An option related with the best customer (who has booked/bought more)
    print("0) EXIT")
    print("----------------------------------------------------")
    menuOption = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")

    if menuOption == 1:
        menuEnployees()
    elif menuOption == 2:
        menuCustomers() 

    elif menuOption == 3:
        print("-------------------- MENU BOOKINGS -------------------------")
        print("---------------What do you want to book?:-------------------")
        print("1) Book a cabin") #An option related with the management system of the bookings of cabins
        print("2) Book a service") #An option related with the management system of the bookings of services
        print("0) EXIT")
        
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")
        if answer == 1:
            menuBookCabin()
        #elif answer == 2:
            #menuBookService()


    elif menuOption == 4:
        menuservices()

    elif menuOption == 5:
        menucabins()

    elif menuOption == 6:
        menuproducts()

    elif menuOption == 0:
        print("Goodbye!")
        input("Press enter to close...")
    else:
        print("invalid number")

