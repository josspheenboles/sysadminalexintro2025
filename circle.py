from shape import Shape
class Circle(Shape):
    count=0
    def __init__(self,rad):
        super().__init__('c',rad)
        Circle.count+=1
    #override
    def calarea(self):
        return 3.14*self.rad**2