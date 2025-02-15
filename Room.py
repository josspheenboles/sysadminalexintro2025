class Instructor:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    #assocation
    def usewihitboard(self,marker):
        pass
#compision relation
class Room:
    def __init__(self,*objectswall):
        self.left=objectswall[0]
        self.right=objectswall[1]
        self.back=objectswall[2]
        self.up=objectswall[3]
        
    # instructor enterd room for time
    #aggeration
    def used(self,instructorref):
        print(f'{instructor.name} entered')
    