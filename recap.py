from abc import ABC,abstractmethod
from multipledispatch import dispatch
#abstract class
class Shape(ABC):
    count=0
    def __init__(self ,name,d1,d2=0):
        self.name=name
        self.d1=d1
        self.d2=d2
        Shape.count+=1
    @abstractmethod
    def calcarea():
        pass
#multilevel inher
class Rect(Shape):
    count=0
    def __init__(self, d1, d2):
        Rect.count+=1
        return super().__init__('r', d1, d2)
    
    #override
    def calcarea(self):
        return self.d1*self.d2
    #override operator
    def __add__(self,other):
        thirdrect=Rect(self.d1+other.d1,self.d2+other.d2)
        return thirdrect
    #magical 
    def __str__(self):
        return f'Rect \n width :{self.d1} \n length={self.d2}'
    def __len__(self):
        return (self.d1+self.d2)*2
    @dispatch(int,int)
    def add(self,x,y):
        print(x,y)
    @dispatch(float,float)
    def add(self,x,y):
        print(x,y)
# obj=Shape('c',1)
obj=Rect(10,20)
obj2=Rect(8,16)
obj3=obj2+obj
print(obj3)
print(len(obj))
# print(obj.calcarea())
# print(Shape.count,Rect.count)