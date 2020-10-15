class User:   
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    def getName(self): return self.name
    def getPassword(self): return self.password
    def sendMessage(self, message): print(message,"sent to",self.email)




class WebLogin():
    def __init__(self):
        #Use username as key
        self.users = {}
    def addUser(self, name, password, email):
        self.users[name] = User(name,password,email)
            
    def login(self, name, password):
        if not name in self.users:
            return False
        
        u = self.users[name]
        if u.getPassword() == password:
            return True
        return False

    def sendPassword(self, name):
        if not name in self.users:
            return False
        u = self.users[name]
        u.sendMessage("Your password is: {}".format(u.getPassword()))
