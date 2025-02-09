class Human:
    count=0
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.__age=age
        Human.count+=1
    def eat(self):
        print('eated')
    def display(self):
        print(f'Name:{self.fname} {self.lname} \nAge:{self.__age}\n')

class Employee(Human):#salary
    count=0
    def __init__(self, fname, lname, age,salary):
        super().__init__(fname, lname, age)        
        self.salary=salary
        Employee.count+=1
    def display(self):
         super().display()
         print(f'Salary:{self.salary}')
#child --->??
H=Human('11','11',22)
emp=Employee('aya','ali',23,5000)

print(Human.count)
print(Employee.count)
# emp.display()
# emp.eat()