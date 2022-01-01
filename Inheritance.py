class vehicle:
    def general_use(self):
        print('General use of vericle is to provide transportation')
class car(vehicle): #writting name of parent class in parenthesis tells us that we are inhering the properties from that class
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.roof = True

    def specific_use(self):
        self.general_use()
        print('Specific use of car:  go for vacation with family')

class motorcycle(vehicle): #we are deriving property from vehicle to mortorcycle
    def __init__(self):
        print('I am Motorcycle')
        self.wheels = 2
        self.roof = False

    def specific_use(self):
        self.general_use()
        print('Road Trips')

c = car()
c.specific_use()

m = motorcycle()
m.specific_use()

#Benifits : Reuse ,Extensibility, Readability

print(isinstance(c,motorcycle)) #to check that the perticular instance fall in specific class or not
print((issubclass(motorcycle,vehicle))) # checks if perticular class is subclass of specific class or not

#EXERCISE
#QNO 1

class Animal:
    def __init__(self,habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)
    def sound(self):
        print('Some animal sounds')
class dog(Animal):
    def __init__(self):
        super().__init__('kennel')
    def sound(self):
        print('woof woof')

x = dog()
x.print_habitat()
x.sound()