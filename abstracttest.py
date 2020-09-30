from abc import ABC, abstractmethod 
  
class Polygon(ABC):
    
    def numofsides(self): 
        pass
  
class Triangle(Polygon): 

    def numofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    def numofsides(self): 
        print("I have 5 sides") 
 
V = Triangle() 
V.numofsides() 
  
K = Pentagon() 
K.numofsides() 
