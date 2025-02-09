from Human import *
humanobj=Human('aya','ali',20)
empobj=Employee('ali','sayed',90,5000,'Sys admin')
# empobj.fun()
empobj.display()

# # import Human
# # obj=Human.Human('d','d',3)
# import socket
# import sys
# ip=sys.argv[1]
# hostnamet=socket.gethostbyname(ip)
# s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# for port in range(1,65535):
#     try:
#         res=s.connect_ex((hostnamet,port))
#         # sleep(1)
#         if(res==0):
#             f=open(f'server{ip}.log','a')
#             f.write(f'port {post} is open\n')
#             f.close()
#     except socket.gaierror:
#         print('invalid ip')
#     except KeyboardInterrupt:
#         print('some one canc el sript')
#     except socket.error:
#         print('connection error')
#     else:
#         print('all port checked')

# # from Human import *

# # obj1=Human('aya','ali',22)
# # obj2=Human('ahmed','ali',25)
# # obj3=Human('mark','amgad',-20)#
# # print(obj1._lname)
# # # obj1.display()
# # # obj2.display()
# # # Human.getcount()
# # # Human.measuretemp(37)
# # # obj1.measuretemp(28)


# # # measuretemp--->logic realted to human class & implement related  to human
# # # obj1.getcount()

# # print(Human.count)
# # print(obj1.count)
# # print(obj2.count)
# # obj2.count=0 #convert count var from class to instance

# print(obj1.fname ,obj1.lname,obj1.age)
# print(obj2.fname ,obj2.lname,obj2.age)

# print(f'Name: {obj1.fname} {obj1.lname} \n Age:{obj1.age}')

# obj1.eat()
# obj2.eat()

# print(obj1)
# obj1.eat()
# print(obj2)
# obj2.eat()
