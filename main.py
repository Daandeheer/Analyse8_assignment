import abc

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
        while True:
            try:
                name = input(clientInput)
            except ValueError:
                print("")
                continue
            if len(name) < 5 or len(name) > 30:
                print("A name requires at least 5 and at most 30 characters")
                continue
            elif not all(x.isalpha() or x.isspace() for x in name):
                print("Name can only contain letters")
                continue
            else:
                break
        return name


    def AddClient(self):
        cityList = ["Amsterdam", "Rotterdam" ,"Maastricht", "Eindhoven", "Den Haag", "Utrecht" ,"Leiden", "Arnhem", "Zwolle","Delft"]
        if self.accessLevel == "system admin":
            print('Status: System administrator can add a new Client')
            print('Add the following information to register as a client')
            
            
            fullName = self.NameValidation("Full name: ")
            streetName = input("Street: ")
            HouseNumber = input("Housenumber: ")
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