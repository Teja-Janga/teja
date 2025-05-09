#ABSTRACTION CLASS
#An abstract class is a class that cannot be instantiated on its own and serves as a blueprint for other classes.
#It can contain abstract methods, which are methods declared without implementation. Subclasses must implement these abstract methods.

#In python we cannot create Abstraction Class directly.
#For that we need to import package "abc" and from that we need to access "ABC" Abstaction Base Class and a method called "abstractionmethod" 

from abc import ABC, abstractmethod #importing "abc package" and "ABC class" and "abstractionmethod method"

class Demo(ABC):
    @abstractmethod
    def calculate(self):
        pass

class A(Demo):
    def calculate(self,a):
        print("a = ",a)
        print ("square of that number = ", a*a)

o=A()
o.calculate (10)