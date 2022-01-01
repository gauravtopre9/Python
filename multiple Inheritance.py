#way One
class father:
    def gardening(self):
        print('I enjoy Gardening')

class mother:
    def cooking(self):
        print('I enjoy Cooking')

class child(father,mother):
    def sport(self):
        print("I enjoy Sports")

c = child()
c.gardening()
c.cooking()
c.sport()


#way TWo
class Father:
    def skills(self):
        print('My skill is Gardening')
class Mother:
    def skills(self):
        print('My skill is cooking')
class Child(father,mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c1 = Child()
c1.skills()