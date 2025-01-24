#class Claculatar:
 #   def__init__(self,n):
  #  self.n = n   
   # def squere(self):
    #    print(f"The squre of {self.n*self.n}")

#a = Calculator(4)
#a.squre()
class Calculator:  
    def __init__(self, n):  
        self.n = n  # Proper indentation for the constructor

    def square(self):  # Corrected method name spelling
        print(f"The square of {self.n} is {self.n * self.n}")  # Corrected message format

a = Calculator(100)  # Corrected class name spelling
a.square()  
