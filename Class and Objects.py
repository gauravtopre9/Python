#CLASS : Class is nothing but abstraction of some entities which contains properties and methods

#OBJECT : object is specific instance of class

#writing class
class Human:
    def __init__(self,name,occupation): #this line initiate the class in which we will define properties of that class
        '''
        Self here means the class itself
        '''
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == 'tennis':
            print(self.name,'Plays Tennis')
        elif self.occupation == 'actor':
            print(self.name,'do TV serials')
        else:
            print(self.name, 'is not doing anything')
    def speaks(self):
        print(self.name,'Says Hi')

tom = Human('tom','tennis')
tom.do_work()
tom.speaks()

sam = Human('sam','actor')
sam.do_work()
sam.speaks()

#EXERCISE

#Q.no1
class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print(f"id: {self.id}\nName: {self.name}")

emp = Employee(1,'coder')
emp.display()

del emp.id

try:
    print(emp.id)
except Exception as e:
    print('emp.id not exists')
    print(e)

del emp

try:
    emp.display()
except Exception as e:
    print('Emp is deleted')
