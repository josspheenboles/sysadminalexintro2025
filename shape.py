from abc import abstractmethod,ABC
class Shape(ABC):
    count=0
    def __init__(self,name,dim1,dim2=0):
        self.name=name
        self.dim1=dim1
        self.dim2=dim2
        Shape.count+=1
    @abs
    def calcarea(self):
        pass
        # if(self.name=='c'):
        #     return 3.14*self.dim1**self.dim1
        # elif(self.name=='s'):
        #     return self.dim1*self.dim1
        # elif(self.name=='r'):
        #     return self.dim1*self.dim2
        # elif(self.name=='t'):
        #     return .5*self.dim1*self.dim1
        # else:
        #     return 'invalid shape name'