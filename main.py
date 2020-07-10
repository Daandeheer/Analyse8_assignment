import abc
import Db
import re
import logging

logging_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= "system.log",
                    level= logging.DEBUG,
                    format = logging_format,
                    filemode= 'w')
logger = logging.getLogger()

logger.info("log")
                            

class User(abc.ABC):
    def __init__(self, username):
        self.username = username

    
class SuperAdmin(User):
    def __init__(self, username):
        super().__init__(username)
        self.accessLevel = "super admin"

    def createSysAdmin(self):
        username = System.UsernameValidation("Please enter a username: ")
        if Db.check_username_exists(username):
            password = System.PasswordValidation("Please enter a password: ")
            Db.create_user(username, password, "system admin")
            print("System admin has been created.")
        else:
            print("Username already exists. Please enter another username.. ")
            return self.createSysAdmin()

class SysAdmin(User):
    def __init__(self, username):
        super().__init__(username)
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
    def __init__(self, username):
        super().__init__(username)
        self.accessLevel = "advisor"


class System :
    
    @staticmethod
    def Login():
        attemps = 0
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        result = Db.auth_login(username, password)
        if result != None:
            print("Logged in successful!")
            if result[1] == "super admin":
                return SuperAdmin(result[0])
            elif result[1] == "system admin":
                return SysAdmin(result[0])
            elif result[1] == "advisor":
                return Advisor(result[0])

            
        else:
            print("Login credentials are incorrect. Please try again..")
            attemps = attemps + 1
            return System.Login()
    
    @staticmethod
    def UsernameValidation(userInput):
        username = input(userInput)
        output = re.search("^[a-zA-z][a-zA-Z0-9-_'.]{4,19}$", username)
        if output == None:
            print("Username needs at least 5 characters and must be started with a letter")
            return System.UsernameValidation(userInput)
        else:
            return username

    @staticmethod
    def PasswordValidation(userInput):
        password = input(userInput)
        output = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[+='|\(}){:;<[>,.?~!@#$%^&*_-])[A-Za-z\d+='|\(}){:;<[>,.?~!@#$%^&*_-]{8,30}$", password)
        if output == None:
            print("Password needs at least 8 characters and at least 1 lower and 1 uppercase letter, 1 digit and 1 special character")
            return System.PasswordValidation(userInput)
        else:
            return password



def main():
    Db.main()
    Db.create_init_user()
    loggedin = System.Login()

    # superadmin.createSysAdmin()

main()
