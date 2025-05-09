#If a function is defined inside a class it is a "METHOD", if it is defined outside of the class it is "FUNCTION" 
class Demo:
    def m1(self): #Inorder to return something by the class a parameter should be given to function if no parameter is there we'll give default parameter "self"
        print("This is a basic example on Class & Object")
o=Demo() #This is Object defined for the class called "Demo" and "o" is a reference variable 
o.m1() #for executing function need to be called but here function is inside the class so we need to use reference variable to make function call