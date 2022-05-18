import Booking
import Basic_Metods

class BookingCabin(Booking.Booking):
    def __init__(self, id,d, hourIn, hourOut, cus, c, p, a): #Constructor

        super.__init__(id,d, hourIn, hourOut, cus, c, p)
        self.available = a
        
        
    def setavailable(self):
        self.available = Basic_Metods.BasicMethods.askAString("Enter the new availability:\n")  
        
    def getavailable(self):
        return self.available

    def toString(self):
        print(self.id,self.date,self.hourIn,self.hourOut, self.cusID, self.cabinID, self.price, self.available)