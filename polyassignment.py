class User:
    name = "Rob"
    email = "robbob@hotmail.com"
    password = "123456"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome ya scrub, {}".format(entry_name))
        else:
            print("Bro you hacking?")

class Dude(User):
    dude_age = 21
    bro_status = "Major"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_status = input("What's your bro status: ")
        if (entry_email == self.email and entry_status == self.bro_status):
            print("Suh dude {}".format(entry_name))
        else:
            print("You sketch bruh")

class Friend(User):
    friend_age = 30
    friend_type = "Super"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_status = input("How much of a friend are you? ")
        if (entry_email == self.email and entry_status == self.friend_type):
            print("You're such a nice friend {}".format(entry_name))
        else:
            print("Are you really my friend?")


customer = User()
customer.getLoginInfo()

bruh = Dude()
bruh.getLoginInfo()

friend = User()
friend.getLoginInfo()
