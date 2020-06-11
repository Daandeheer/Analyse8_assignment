import abc
import re

class User(abc.ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class SuperAdmin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "super admin"
        
        
class SysAdmin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "system admin"

    def NameValidation(self, clientInput):
        fullName = input(clientInput)
        output = re.search("^[a-z, \s]{5,31}$", fullName)
        if output == None:
            print("A name requires at least 5 and at most 30 characters")
            return self.NameValidation(clientInput)
        else:
            return fullName
        

    def StreetNameValidation(self, clientInput):
        streetName = input(clientInput)
        output = re.search("^[a-z, \s]{5,31}$", streetName)
        if output == None:
            print("A name requires at least 5 and at most 30 characters")
            return self.StreetNameValidation(clientInput)
        else:
            return streetName
        
    
    def HouseNumberValidation(self, clientInput):
        houseNumber = input(clientInput)
        output = re.search("^[1-9]([0-9]{0,3})[a-z]?$", houseNumber)
        if output == None:
            print("House Number can only have a maximum of 4 digits and optionally 1 letter")
            return self.HouseNumberValidation(clientInput)
        else:
            return houseNumber
        
        


    def AddClient(self):
        cityList = ["Amsterdam", "Rotterdam" ,"Maastricht", "Eindhoven", "Den Haag", "Utrecht" ,"Leiden", "Arnhem", "Zwolle","Delft"]
        if self.accessLevel == "system admin":
            print('Status: System administrator can add a new Client')
            print('Add the following information to register as a client')
            
            
            # fullName = self.NameValidation("Full name: ")
            # streetName = self.StreetNameValidation("Street: ")
            houseNumber = self.HouseNumberValidation("Housenumber: ")

            # zipCode = input("Zip code: ")
            # city = input("Choose one of the Citys " + str(cityList) + ": ")
            # emailAddress = input("Email Address: ")
            # phoneNumber = input("Phone Number: ")
            

        elif self.accessLevel == "super admin":
            print("Status: Super administrator has no access to add a new Client")

        else:
            print("Status: Advisor has no access to add a new Client")



class Advisor(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "advisor"


def main():
    superadmin = SuperAdmin("User", "Pass")
    sysadmin = SysAdmin("User", "Pass")
    advisor = Advisor("User", "Pass")
    test = sysadmin.AddClient()

main()