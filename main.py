import abc
import Db
import re

# regex email
# regex password --> delete file database, use count
# regex username --> delete file database, use count

class User(abc.ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def UsernameValidation(self, userInput):
        usernameAttemps = 0
        username = input(userInput)
        output = re.search("^[a-zA-z][a-zA-Z0-9-_'.]{4,19}$", username)
        if output == None:
            print("Wrong input")
            usernameAttemps = usernameAttemps + 1
            return self.UsernameValidation(userInput)
        else:
            return username
        

    
    def PasswordValidation(self):
        pass

class SuperAdmin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "super admin"

    def createSysAdmin(self, username, password):
        Db.create_user(username, password, "system admin")
        print("System admin has been created.")

superuser = SuperAdmin("super", "super")

class SysAdmin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "system admin"

    def createAdvisor(self, username, password):
        Db.create_user(username, password, "advisor")
        print("Advisor has been created.")

    def NameValidation(self, clientInput):
        fullName = input(clientInput)
        output = re.search("^[a-zA-Z, \s]{5,31}$", fullName)
        if output == None:
            print("Invalid input: A name requires at least 5 and at most 30 characters, please try again:")
            return self.NameValidation(clientInput)
        else:
            return fullName

    def StreetValidation(self, clientInput):
        street = input(clientInput)
        output = re.search("^[a-zA-Z, \s]{5,31}\s[1-9]([0-9]{0,3})[a-z]?$", street)
        if output == None:
            print("Invalid input: Street requires at least 5 and at most 30 characters. Also don't forget to include your house number, please try again:")
            return self.StreetValidation(clientInput)
        else:
            return street

    def ZipCodeValidation(self, clientInput):
        zipCode = input(clientInput)
        output = re.search("^[1-9][0-9]{3}[A-Z]{2}$", zipCode)
        if output == None:
            print("Invalid input: Use capital letters and remove space, please try again:")
            return self.ZipCodeValidation(clientInput)
        else:
            return zipCode

    def CityValidation(self, clientInput):
        cityList = ["Amsterdam", "Rotterdam" ,"Maastricht", "Eindhoven", "Den Haag", "Utrecht" ,"Leiden", "Arnhem", "Zwolle","Delft"]
        print(cityList)
        city = input(clientInput)
        for x in cityList:
            if re.search(x, city) :
                return city
            else:
                print("Invalid input: City don't exist, please choose a city from the list:  (City begins with a capital letter)")
                return self.CityValidation(clientInput)

    # Add regex for email
    def EmailValidation(self, clientInput):
        emailAddress = input(clientInput)
        output = re.search("^[0-9a-zA-Z]{2,20}@[a-zA-z]+\.[a-zA-z]{2,10}",emailAddress)
        if output == None:
            print("Invalid input: Use a real email, please try again:")
            return self.EmailValidation(clientInput)
        else:
            return emailAddress

    def PhoneNumberValidation(self,clientInput):
        phoneNumber = input(clientInput)
        output = re.search("^[+][3][1][6][0-9]{8}$",phoneNumber)
        if output == None:
            print("Invalid input: Start with +316, please try again:")
            return self.PhoneNumberValidation(clientInput)
        else:
            return phoneNumber


    def AddClient(self):
        if self.accessLevel == "system admin":
            print('Status: System administrator can add a new Client')
            print('Add the following information to register as a client')



            # fullName = self.NameValidation("Full name: ")
            # street = self.StreetValidation("Street: ")
            # zipCode = self.ZipCodeValidation("Zip code: ")
            # city = self.CityValidation("Choose one of the Citys: ")
            # emailAddress = self.EmailValidation("Email Address: ")
            # phoneNumber = self.PhoneNumberValidation("Phone Number: ")


        elif self.accessLevel == "super admin":
            print("Status: Super administrator has no access to add a new Client")

        else:
            print("Status: Advisor has no access to add a new Client")


class Advisor(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "advisor"

def Login():
    username =  self.User.UsernameValidation("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == superuser.username and password == superuser.password:
        print("Logged in as super user")
    else:
        print("Login credentials are incorrect. Please try again..")
        return Login()

def main():
    Db.main()
    Login()

    superadmin = SuperAdmin("User", "Pass")
    sysadmin = SysAdmin("User", "Pass")
    advisor = Advisor("User", "Pass")
    sysadmin.AddClient()

main()
