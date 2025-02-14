class Point:
    def __init__(self,x,y):
        # self.setx(x)
        self.x=x
        # self.sety(y)
        self.y=y
    #magical functions
    def __len__ (self):
        #retun number
        return self.x+self.y
    def __str__(self):
        #return string 
        return f'({self.__x},{self.__y})'
    #==============getter as property
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    #==============setter as property
    @x.setter
    def x(self,newvalue):
        if(newvalue is not None):
            self.__x=newvalue
        else:
            self.__x=0
    @y.setter
    def y(self,newvalue):
        if(newvalue is not None):
            self.__y=newvalue
        else:
            self.__y=0
    #==============setter as instance method
    # def setx(self,newvalue):
    #     if(newvalue is not None):
    #         self.__x=newvalue
    #     else:
    #         self.__x=0
    def sety(self,newvalue):
        if(newvalue is not None):
            self.__y=newvalue
        else:
            self.__y=0
  
    #==============getter as instance method
    # def getx(self):
    #    return self.__x
    # def gety(self):
    #    return self.__y

class Line:
    def __init__(self,p1,p2):
        self.startppoint=p1
        self.endpoint=p2
    def __str__(self):
        # print(self.startppoint)
        return f'''start:({self.startppoint.x},{self.startppoint.y})
        end:({self.endpoint.x},{self.endpoint.y})'''
p1=Point(10,20)
p2=Point(10,30)
l=Line(p1,p2)
print(l)
# p1=Point(10,100)
# print(p1)
# print(len(p1))
#display x,y

# print(p1.x,p1.y)

# #change x,y
# p1.x=10
# # p1.setx(10)
# # p1.sety(100)
# p1.y=100
# print(p1.x,p1.y)
# print(p1)
# print([1,2],{},(),2,2.2,True)
# #     @property
#     def x(self):
#         return self.__x
#     @x.setter
#     def x(self,xvalue):
#         if(xvalue is not None):
#             self.__x=xvalue
#         else:
#             print('x cannt be none ----')
#             self.__x=0    
#     # #set x
#     # def setx(self,x):
#     #     if(x is not None):
#     #         self.__x=x
#     #     else:
#     #         print('x cannt be none ')
#     #         self.__x=0
#     #get x
#     def getx(self):
#         return self.__x
#      #set y
#     def sety(self,y):
#         if(y is not None):
#             self.__y=y
#         else:
#             print('y cannt be none ')
#             self.__y=0
#     #get y
#     def gety(self):
#         return self.__y

#     def display(self):
#         print(f'({self.__x},{self.__y})')

# p1=Point(1,2)
# p1.display()
# p2=Point(None,1)
# p2.display()
# p1.x=10#call x --->@x.setter
# print(p1.x)
# # # print(p1.__x)
# # print(p1.getx(),p1.gety())