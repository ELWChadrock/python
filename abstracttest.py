from abc import ABC, abstractmethod
class Bro(ABC):
  def bro_slip(self, amount):
    print('Purchase of amount- ', amount)
  @abstractmethod
  def bro(self, amount):
    pass

class BroNumber(Bro):
  def bro(self, amount):
    print('Bro status of- ', amount)

class BroLegitNum(Bro):
  def bro(self, amount):
    print('Bro legit like- ', amount)

obj = BroNumber()
obj.bro(100)
obj.bro_slip(100)
print(isinstance(obj, Bro))
obj = BroLegitNum()
obj.bro(200)
obj.bro_slip(200)
print(isinstance(obj, Bro))
