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


def Login(username, password):
    pass


def main():
    Db.main()
    superuser = SuperAdmin("super", "super")
    superuser.createSysAdmin("sysadmin", "sysadmin")

main()
