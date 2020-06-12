import abc
import Db
import re

# extra validation steps:
# look at capital letters, fails at the moment
# It is possible to add to spaces next to eachother
# city needs to be written exactly like in the list

class User(abc.ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def UsernameValidation(self):
        pass

    def PasswordValidation(self):
        pass

class SuperAdmin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "super admin"

    def createSysAdmin(self):
        username = input("Please enter a username: ")
        # TODO Username validation
        if Db.check_username_exists(username):
            # TODO Password validation
            password = input("Please enter a password: ")
            Db.create_user(username, password, "system admin")
            print("System admin has been created.")
        else:
            print("Username already exists. Please enter another username.. ")
            return self.createSysAdmin()

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
        output = re.search("^[a-z, \s]{5,31}$", fullName)
        if output == None:
            print("Invalid input: A name requires at least 5 and at most 30 characters, please try again:")
            return self.NameValidation(clientInput)
        else:
            return fullName

    def StreetValidation(self, clientInput):
        street = input(clientInput)
        output = re.search("^[a-z, \s]{5,31}\s[1-9]([0-9]{0,3})[a-z]?$", street)
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
                print("Invalid input: City don't exist, please choose a city from the list:")
                return self.CityValidation(clientInput)

    # Add regex for email
    def EmailValidation(self, clientInput):
        emailAddress = input(clientInput)
        output = re.search("",emailAddress)
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

            fullname = self.NameValidation("Full name: ")
            street = self.StreetValidation("Street: ")
            zipcode = self.ZipCodeValidation("Zip code: ")
            city = self.CityValidation("Choose one of the Citys: ")
            emailaddress = self.EmailValidation("Email Address: ")
            phonenumber = self.PhoneNumberValidation("Phone Number: ")

            Db.create_client(fullname, street, zipcode, city, emailaddress, phonenumber)


        elif self.accessLevel == "super admin":
            print("Status: Super administrator has no access to add a new Client")

        else:
            print("Status: Advisor has no access to add a new Client")


class Advisor(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "advisor"

def Login():
    # username = input("Please enter your username: ")
    # password = input("Please enter your password: ")
    if 1 == 1:
        pass
    else:
        print("Login credentials are incorrect. Please try again..")
        return Login()

def main():
    Db.main()
    Login()

    superadmin = SuperAdmin("User", "Pass")
    sysadmin = SysAdmin("User", "Pass")
    advisor = Advisor("User", "Pass")

    superadmin.createSysAdmin()
    # sysadmin.AddClient()

main()
