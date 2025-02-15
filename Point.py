class Point:
    def __init__(self,x,y):
            #private
            self.__x=x
            self.__y=y
    @property
    def x(self):
          return self.__x
#     def x(self,newvalue)
# 2int--->object Point boxing(x,y)
# accses object--->unboxing