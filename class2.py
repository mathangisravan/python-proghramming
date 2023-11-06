
class person :

    def __init__(self,name,age):
          self.name = name
          self.age = age
    def compare(self,other):
        if self.age == other.age:
            return True
        else :
            return False
    
m1 = person(name = 'Sravan',age = 21)
m2 = person(name = 'Bokka', age = 21)

if m1.compare(m2):
        print('They are same')
else:
        print('They are not same')
