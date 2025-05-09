#A variable that is defined inside a class before defining the method is called "Static or Class Variable". 
#In below code snippet "bank_name" is the Class Variable.
class Bank:

    bank_name="Andhra Bank"
    def Display(self):
        print(Bank.bank_name) #Inorder to print the Class Variable we need to write the variable name along with classname in the print statement.
    def Update(self):
        Bank.bank_name="Union Bank"

Raju=Bank()
Ramu=Bank()
#Here Raju & Ramu are the objects of the class called "Bank".
Raju.Display()
Raju.Update()
Raju.Display()
#Here we updated the value of Class Variable with object called "Raju".
Ramu.Display()

#NOTE: With Static or Class Variable if we update the value of Class Variable with one object,
#it will effect the value of all the objects that are defined to that class.