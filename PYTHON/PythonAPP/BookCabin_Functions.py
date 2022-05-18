import pickle
import Basic_Metods
import BookingCabin

def menuBookCabin():
    menuBOOKOption = -1
    print("For the management system of the bookings what file do you want to use?")
    fileName = Basic_Metods.BasicMethods.askForFile()
    while (menuBOOKOption != 0):
        print("\n--------------------MENU CABIN BOOKINGS-----------------------")
        print("1) Update a booking")
        print("2) Delete a booking")
        print("3) Insert a new booking and save on a file")
        print("4) See all the bookings")
        print("0) Exit")
        print("--------------------------------------------------------------\n")
        menuBOOKOption = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")
        if menuBOOKOption == 1: #Update a Booking
            updateABooking(fileName)
        elif menuBOOKOption == 2: #Delete a Booking
            deleteABooking(fileName)
        elif menuBOOKOption == 3: #Insert new Booking  #Save the Booking on a file 
            saveAndCreateTheBookings(fileName)
        elif menuBOOKOption == 4: #See all the Bookings
            seeAllTheBookings(fileName)

def createANewBooking():
    print("\n---------------------------------------------------------------------")
    print("---------------- You are going to CREATE a booking.--------------------")
    print("---------------------------------------------------------------------\n")
    id = Basic_Metods.BasicMethods.askAString("Enter the ID: \n")
    date = Basic_Metods.BasicMethods.askAString("Enter the date: \n")
    hourIn = Basic_Metods.BasicMethods.askAString("Enter the hour in: \n")
    hourOut = Basic_Metods.BasicMethods.askAString("Enter the hour out: \n")
    cusID = Basic_Metods.BasicMethods.askAString("Enter the customer ID: \n")
    cabinID = Basic_Metods.BasicMethods.askAnInt("Enter the cabin ID: \n")
    available = Basic_Metods.BasicMethods.askAString("Enter the availablility: \n")
    price = Basic_Metods.BasicMethods.askAnDouble("Enter the price: \n")

    cabinBooking = BookingCabin.BookingCabin(id, date, hourIn, hourOut, cusID, cabinID, available, price)
    return cabinBooking

def seeAllTheBookings(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------- You are going to SEE all the bookings.----------------")
    print("---------------------------------------------------------------------\n")
    Basic_Metods.BasicMethods.readFile(fileName)
        
    
def saveAndCreateTheBookings(fileName):
    ans = 1
    while ans == 1:
        b1 = createANewBooking()
        print("\n---------------------------------------------------------------------")
        print("----------------------- SAVING the booking... -------------------------")
        print("---------------------------------------------------------------------\n")
        Basic_Metods.BasicMethods.save_objectOn_File(b1,fileName)
        ans = Basic_Metods.BasicMethods.askAnInt("Do you want to add a new booking? (1/0)")
    del b1

def deleteABooking(fileName):
    bookings = []
    seeAllTheBookings(fileName)
    print("Which booking you want to delete?")
    bookingID = Basic_Metods.BasicMethods.askAString("Enter the booking ID of the booking:\n")
    pos = searchByBookingID(fileName, bookingID)
    if pos != -1:
        bookings = Basic_Metods.BasicMethods.readFileToList(fileName)
        bookings.pop(pos)
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, bookings)
    else:
        print("The customer does not exist.")
   
def searchByBookingID(fileName, id):
        inp = open(fileName, 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                cont = 0
        i = 0
        answer = -1
        for st in objects:
            if st.id == id:
                answer = i
            i = i + 1
        return answer
        
def updateABooking(fileName):
    bookings = []
    seeAllTheBookings(fileName)
    print("Which booking you want to update?")
    bookingID = Basic_Metods.BasicMethods.askAString("Enter the booking ID of the booking:\n")
    pos = searchByBookingID(fileName, bookingID)
    if pos != -1:
        bookings = Basic_Metods.BasicMethods.readFileToList(fileName)
        print("\n-----------------Enter the new information of the booking-----------------\n")
    
        print("Do you want to change the booking ID? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            bookings[pos].setid()
            
        print("Do you want to change the date? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            bookings[pos].setdate()
            
        print("Do you want to change the hour in? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            bookings[pos].sethourIn()
            
        print("Do you want to change the hour out? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            bookings[pos].sethourOut()
            
        print("Do you want to change the customer id? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            bookings[pos].setcusID()
        
        print("Do you want to change the cabin id? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            bookings[pos].setcabinID() 
            
        print("Do you want to change the availablility? (1/0)") 
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            bookings[pos].setavailale()
            
        print("Do you want to change the price? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            bookings[pos].setprice()
            
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, bookings)
    else:
        print("The booking does not exist.")
