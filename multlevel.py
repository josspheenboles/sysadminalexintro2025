class Human:
    coun=0 #count human
    def __init__(self,id,name,gender):
        self.name=name
        self.id=id
        self.gender=gender
        print('iam human constr')
    def diaply(self):
        return(f'iam {self.name}')
class Employee(Human):
    count=0#count employee
    def __init__(self, id, name, gender,salary,position):
        
        self.salary=salary
        self.position=position

        print('iam emplooye constr')
        super().__init__(id, name, gender)
    def diaply(self):
        print(super().diaply()+ f",Pos:{self.position}")
#inheitance from employee--->Human
# class Sysadmin(Employee):
#     pass

class Sysadmin(Human,Employee):
    pass

# obj=Sysadmin(1,'ali','M',5000,'sen.')
# obj.diaply()
obj=Sysadmin(1,'ali','M')
# obj.