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
        if (entry_email == self.email and entry_pin == self.bro_status):
            print("Suh dude {}".format(entry_name))
        else:
            print("You sketch bruh")

customer = User()
customer.getLoginInfo()

bruh = Dude()
bruh.getLoginInfo()
