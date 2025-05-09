# Instance Variable is used when the data is unique. Like a Bank Customer will have unique account number, address, phone number.
# In such cases instance variable is used.
#Instance Variable is defined inside a method. 
class Bank:

    bank_name="Andhra Bank" #Static Variable

    def load(self):
        self.accountnum= 2010100020 #For defining Instance Variable we need to use "self". => "self.variable_name"
        self.phonenum=9848032919 #Instance Variable
        self.address= "Nandyal"

    def Display(self):
        print(self.accountnum)
        print(self.phonenum)
        print(self.address)
        print(Bank.bank_name) 
    def Update(self):
        Bank.bank_name="Union Bank"
   
Raju=Bank()
Ramu=Bank()
#After defining the object for class we need to call the method in which the instance variable is defined first,
#so that the instance variable will be stored in the object then we can use them to print
Raju.load()
Ramu.load()

Raju.Display()
Raju.Update()
print()
Raju.Display()
print()
Ramu.Display()