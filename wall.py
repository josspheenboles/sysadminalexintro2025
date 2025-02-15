class Wall:
    def __init__(self,w,h):
        self.Width=w
        self.Height=h
    @property
    def Height(self):
        return self.__height
    @Height.setter
    def Height(self,value):        
        if(value>0):
            self.__height=value
        else:
            print(f'height must be graatr than {value}')
    @property
    def Width(self):
        return self.__width
    @Width.setter
    def Width(self,value):

        if(value>0):
            self.__width=value
        else:
            print(f'width must be graatr than {value}')
    def __str__(self):
        return f'{self.Width} * {self.Height}'