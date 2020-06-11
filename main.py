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


class Advisor(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.accessLevel = "advisor"


def main():
    superadmin = SuperAdmin("User", "Pass")
    sysadmin = SysAdmin("User", "Pass")
    advisor = Advisor("User", "Pass")
    print(superadmin.accessLevel)
    print(sysadmin.accessLevel)
    print(advisor.accessLevel)

main()