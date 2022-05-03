from Person import *
import Basic_Metods

class Customer(Person):
    def __init__(self, id, name, surname, phone_home, phone_mobile, email, address, city, postcode, condition):
        super().__init__(id, name, surname, phone_home, phone_mobile, email, address, city, postcode, condition)



