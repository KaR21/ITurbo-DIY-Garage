import Basic_Metods
import Booking

class BookingService(Booking.Booking):
    def __init__(self, id,d, hourIn, hourOut, cus, c, p, s, emp, sN): #Constructor

        super.__init__(id,d, hourIn, hourOut, cus, c, p)
        self.serviceID = s
        self.employeeID = emp
        self.serviceName = sN
        
    
    def setserviceID(self):
        self.serviceID = Basic_Metods.BasicMethods.askAString("Enter the new service ID:\n")  
        
    def setempID(self):
        self.employeeID = Basic_Metods.BasicMethods.askAString("Enter the new employee ID:\n")
        
    def setserviceName(self):
        self.serviceName = Basic_Metods.BasicMethods.askAString("Enter the new service name:\n")
    
    
    def getserviceID(self):
        return self.serviceID

    def getempID(self):
        return self.empID
    
    def getserviceName(self):
        return self.serviceName
    
    def toString(self):
        print(super.toString(), self.serviceID, self.employeeID, self.serviceName)
