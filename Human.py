#attributes
#id,name,address,gender,bdate ? --->instance(object) var
#methos (action)
#eat,sleep,breath,look

class Human:
    #class var
    count=0
    #constructuror spacial / magical autocalling
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender
        Human.count+=1
        print('iam human constr')

class Student:
    pass