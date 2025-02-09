# #public
# class Human:
#     count=0
#     def __init__(self,_name,_lname,_age):
#         self.fname=_name
#         self.lname=_lname
#         self.__age=_age
#         Human.count+=1
   
#     def eat(self):
#         print(f'belhan ya {self.fname} {self.lname}')
    
#     def sleep(self):
#         print(f'{self.fname} sleeping')
    
#     def speek(self):
#         print(f'iam {self.fname} {self.lname}')
    
#     def display(self):
#         print (f'Name:{self.fname} {self.lname} \nAge:{self.__age}')

#     @classmethod#function @ declare moethod change behavior
#     def getcount(cls):
#         print(cls)

#     @staticmethod
#     def measuretemp(self,temp):#2 arg
#         if(temp<37):
#             print('v cold')
#         elif (temp >37):
#             print('v hot')
#         else:
#             print('normal')    
# #employee is human
# class Employee(Human):
    
#     def __init__(self,fname,lname,age,salary,position):
#         super().__init__(fname,lname,age)
#         self.salary=salary
#         self.position=position
#     # def fun(self):
#     #     print(self.__age)
#     def display(self):
#         print(super().display())
#         print(f'Salary:{self.salary}\nPosition:{self.position}')
    
# # class ip:
# #     def validateip(self):
# #         pass
# # class Server:
# #     def __init__(self,_servername,_ip,_core,_ram):
# #         self.servername=_servername
# #         if Server.vip(_ip):#calling
# #             self.ip=_ip
# #         self.corsnum=_core
# #         self.ram=_ram
# #         # self.port=_port
    
# #     @staticmethod
# #     def vip(ip):
# #         pass
        
