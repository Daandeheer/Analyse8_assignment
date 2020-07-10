import abc
import Db
import re
import logging
import os

logging_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= "system.log",
                    format = logging_format)
logger = logging.getLogger()

class User(abc.ABC):
    def __init__(self, username):
        self.username = username

    
class SuperAdmin(User):
    def __init__(self, username):
        super().__init__(username)
        self.accessLevel = "super admin"

    def createSysAdmin(self):
        print("Creating a System Administrator..")
        username = System.UsernameValidation("Please enter a username: ")
        if Db.check_username_exists(username):
            password = System.PasswordValidation("Please enter a password: ")
            Db.create_user(username, System.encrypt(password, 5), "system admin")
            print("System admin has been created.")
        else:
            print("Username already exists. Please enter another username.. ")
            return self.createSysAdmin()

class SysAdmin(User):
    def __init__(self, username):
        super().__init__(username)
        self.accessLevel = "system admin"

    def createAdvisor(self):
        print("Creating an advisor..")
        username = System.UsernameValidation("Please enter a username: ")
        if Db.check_username_exists(username):
            password = System.PasswordValidation("Please enter a password: ")
            Db.create_user(username, System.encrypt(password, 5), "advisor")
            print("Advisor has been created.")
        else:
            print("Username already exists. Please enter another username.. ")
            return self.createAdvisor()

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
        
        # cityList = ["Amsterdam", "Rotterdam" ,"Maastricht", "Eindhoven", "Den Haag", "Utrecht" ,"Leiden", "Arnhem", "Zwolle","Delft"]
        # print(cityList)
        # city = input(clientInput)
        # for x in cityList:
        #     if re.search(x, city) :
        #         return city
        print("""
                        [1] Amsterdam
                        [2] Rotterdam
                        [3] Maastricht
                        [4] Eindhoven
                        [5] Den Haag
                        [6] Utrecht
                        [7] Leiden
                        [8] Arnhem
                        [9] Zwolle
                        [10] Delft

                        """)

        city = input("Please enter a number: ")
        if (city == "1"):
            print("City: Amsterdam")
            return "Amsterdam"
        elif (city == "2"):
            print("City: Rotterdam")
            return "Rotterdam"
        elif (city == "3"):
            print("City: Maastricht")
            return "Maastricht"
        elif (city == "4"):
            print("City: Eindhoven")
            return "Eindhoven"
        elif (city == "5"):
            print("City: Den Haag")
            return "Den Haag"
        elif (city == "6"):
            print("City: Utrecht")
            return "Utrecht"
        elif (city == "7"):
            print("City: Leiden")
            return "Leiden"
        elif (city == "8"):
            print("City: Arnhem")
            return "Arnhem"
        elif (city == "9"):
            print("City: Zwolle")
            return "Zwolle"
        elif (city == "10"):
            print("City: Delft")
            return "Delft"
        else:
            print("Invalid input: Number don't exist, please choose a number from the list: ")
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
        print("Creating a client..")
        print('Please enter the following information to register as a client')

        fullname = self.NameValidation("Full name: ")
        street = self.StreetValidation("Streetname: ")
        zipcode = self.ZipCodeValidation("Zip code (format [1111XX]): ")
        city = self.CityValidation("City: (choose a number): ")
        emailaddress = self.EmailValidation("Email address: ")
        phonenumber = self.PhoneNumberValidation("Phone Number: (starting with +316)")

        Db.create_client(fullname, street, zipcode, city, emailaddress, phonenumber)
        print("Client has been registered.")


class Advisor(User):
    def __init__(self, username):
        super().__init__(username)
        self.accessLevel = "advisor"


class System :
    
    @staticmethod
    def Login(attemps=0):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        result = Db.auth_login(username, System.encrypt(password, 5))
        if result != None:
            print("Logged in successful!")
            if result[1] == "super admin":
                return SuperAdmin(result[0])
            elif result[1] == "system admin":
                return SysAdmin(result[0])
            elif result[1] == "advisor":
                return Advisor(result[0])
        elif attemps == 2:
            logger.warning("Too many attemps")
            print("Too many attemps, please try again later.")
            return False
        else:
            print("Login credentials are incorrect. Please try again..")
            return System.Login(attemps+1)
    
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

    @staticmethod
    def read_log():
        print("----------------------------")
        f = open("system.log", "r")
        print(f.read())
        print("----------------------------")

    @staticmethod
    def encrypt(text, n):
        result = ""
        for i in range(len(text)): 
            char = text[i] 
  
            if (char.isupper()): 
                result = result + chr((ord(char) + n - 65) % 26 + 65) 
            elif (not char.isalpha()):
                result = result + char
            else: 
                result = result + chr((ord(char) + n - 97) % 26 + 97) 
  
        return result 

    @staticmethod
    def menu():
        loggedin = False
        while not loggedin:
            print("Welcome to the system. Please select an option to continue: \n[1] Login \n[2] Recover password")
            choice = input("Please select an option: ")
            if (choice == "1"):
                user = System.Login()
                if (user == False):
                    exit()
                loggedin = True
            else:
                print("---That option does not exist (yet). Please try another option.---")
        while loggedin:
            print("Welcome user: %s. Please select one of the following options to continue" % user.username)
            if (user.accessLevel == "super admin"):
                print("""
                        [1] Create system admin
                        [9] Read log
                        [0] Logout
                        """)
                choice = input("Please enter a number: ")
                if (choice == "1"):
                    user.createSysAdmin()
                elif (choice == "9"):
                    System.read_log()
                elif (choice == "0"):
                    print("Your are now logged off..")
                    loggedin = False
                else:
                    print("---Input invalid. Please enter a number presented in the menu.---")
            
            if (user.accessLevel == "system admin"):
                print("""
                        [1] Create advisor
                        [2] Add client
                        [9] Read log
                        [0] Logout
                        """)
                choice = input("Please enter a number: ")
                if (choice == "1"):
                    user.createAdvisor()
                elif (choice == "2"):
                    user.AddClient()
                elif (choice == "9"):
                    System.read_log()
                elif (choice == "0"):
                    print("Your are now logged off..")
                    loggedin = False
                else:
                    print("---Input invalid. Please enter a number presented in the menu.---")
            
            if (user.accessLevel == "advisor"):
                print("""
                        [0] Logout
                        """)
                choice = input("Please enter a number: ")
                if (choice == "0"):
                    print("Your are now logged off..")
                    loggedin = False
                else:
                    print("---Input invalid. Please enter a number presented in the menu.---")
                




def main():
    Db.main()
    Db.create_init_user(System.encrypt("Superpassword1!", 5))
    System.menu()



main()
