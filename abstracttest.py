from abc import ABC, abstractmethod
class loan(ABC):
    def paySlip(self, amount):
        print("Your loan payment: ",amount)
#This function is telling us to pass in an arguement, but we won't tell you how or what kind
#of data it will be
        @abstractmethod
        def payment(self, amount):
            pass


    
class DebitCardPayment(loan):
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $500 limit '.format(amount))

    obj = DebitCardPayment()
    obj.paySlip("$1000")
    obj.payment("$1000")

