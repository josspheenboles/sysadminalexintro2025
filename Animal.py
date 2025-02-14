from abc import abstractmethod,ABC
#class as abstract class
class Animal(ABC):
    count=0
    def __init__(self,name):
        self.name=name
        Animal.count+=1 ####
    def display(self):
        print('iam animal')
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def sound(self):
        pass
        
class Cat(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
    #override 
    def walk(self):
        print('cat walk')
    #override 
    def sound(self):
        print('sound of cat meow')
    #override
    def display(self):
        print('iam cat with marv. colors')
    #operator overloading
    def __add__(self,other):
        return self.age+other.age
    def __mul__(self,other):
        return self.age*self.age
# Animalobj=Animal()
catobj=Cat('catobj',1)
catobj2=Cat('catobj',2)
print(catobj+catobj2)
print(catobj*catobj2)
# catobj.walk()
# catobj.sound()
# catobj.display()