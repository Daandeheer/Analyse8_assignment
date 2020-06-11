import abc
import Db

class User(abc.ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

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
        


class Advisor(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "advisor"

def Option():
    option = int(input("""  
            Welcome to the application.\n 
            Please select an option by entering a number:\n
            [1] Login\n
            [2] Password reset\n
            Your choice: """
    ))
    
    if option == 1:
        Login()

def Login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == superuser.username and password == superuser.password:
        print("Logged in as super user")
    else:
        print("Login credentials are incorrect. Please try again..")


def main():
    Db.main()
    Option()
    

main()
