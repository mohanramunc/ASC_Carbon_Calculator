#This class defines a student organization account.
#Differentiated from a plaid account because mutliple orgs can use the same card
class clubUser:
    def __init__(self, name, password):
        self. name = name
        self.password = password

    def getClubUserName(self):
        return self.name

    def getClubUserPass(self):
        return self.password
