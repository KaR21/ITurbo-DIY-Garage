from Person import Person
import Basic_Metods

class Enployees(Person):
    def __init__(self, ssa):
        super().__init__(self)

        self.Salary = ssa

    def setSalary(self):
            self.Salary = Basic_Metods.BasicMethods.askString("Enter the salary")

    def print(self):
        print(self.Enployee_Id, self.First_name, self.Surname, self.Role, self.Home_Phone, self.Mobile_Phone, self.Email, self.Password, self.Adress, self.City, self.Postcode, self.Condition, self.Salary)
        
