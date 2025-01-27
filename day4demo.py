import sys
try:
    open('py','r')
    print('===')
    open('/asd.txt','a')
    print(1/0)
    n1=int(input('enter num1'))
except ZeroDivisionError:
    print('قسمه ع صفر')
except FileNotFoundError:
    print('قسمه ع صفر')

except:#gerneral excpetc
    print(sys.exc_info()[1])
# Exception parent -->permission,zerdivion
# try:
    # may casuse runtim error
# except :
    # lines handel 
# finally:
# else:
# def fun(n1,n2):
#     res=n1+int(n2)
#     print('jjjkj')

# # n1=10
# # n2='3'
# # fun(n1,n2)
# # #function ,list compreh. , scope,files,errors
# n1=(input('enter number 1'))
# if(n1.isdigit()):
#     n1=int(n1)
#     # print(n1,type(n1))
#     n2=(input('enter number 2'))
#     if(n2.isdigit()):
#         n2=int(n2)
#         print(n1+n2)
#     else:
#         print('n2 must be digit')
# else:
#         print('n1 must be digit')
# print(n2,type)

# # f=open('/asd.txt",'a')
# # f.close()

# # with f as open(path ,mode): #scope end with
# #     read & write operation

# #object declare global scope
# #destory when script end or exit()
# f=open('asd2.txt','r')
# f.close() #destroy f object

# with  open('asd2.txt','r') as f:
#     print(f.read())
#     print(f.read())
#     print(f.read())
#     print(f.read())
# print(f.read())



# #files read & write
# #read analysis string
# #current position of cursor
# #mode



# #rb,rb+
# #r+ --->read & write ,must file exsist
# f=open('asd2.txt','r+')#char0
# f.seek(5)
# #read & write
# f.write('\nr+\n')
# print(f.read())

# f.close()
# #a --->write on end file only,file exsit --->open file seek to end  or not exsist --->create
# # f=open('asd2.txt','a')
# # print(f.read())
# # f.write('lin3\n')
# # f.writelines(['l1\n','l2\n'])
# # f.close()
# #w --->write only,file exsit --->clear or not exsist --->create
# #open w
# f=open('asd2.txt','w')
# # f.write('hi sys admin alex ')
# # f.write('intake45\n')
# # l=['line1\n','line2\n']
# # f.writelines(l)
# f.write('''hi sys admin alx
#         intake45''')
# #close
# f.close()
#r --->read only,file exsist
# # #object=open & path&mode
# streamobj=open('asd2.txt','r')#open cursor on char0
# # streamobj.write('ddd')
# print(type(streamobj),streamobj)
# # content=streamobj.read(4) #countfrom 0 to 4
# # print(content,type(content))
# # print(streamobj.read(5))
# # print(streamobj.read())
# # print(streamobj.readline())
# # print(streamobj.readline())
# # print(streamobj.readline())
# # print('===',streamobj.readline(),'===',sep='&')
# # ===  ====
# # listoflines=streamobj.readlines()
# # print(listoflines)
# for line in streamobj:
#     print(line)
# #close
# streamobj.close()

# open(path,mode)
# #scope in python
# n1=1
# n2=10

# def fun():
#     # global n1
#     n1=1.1
#     print(n1,'fun')
#     def internal():
#         global s1 #
#         s1='pkpkp'#s1
#         print(s1)
#         nonlocal n1 #accsecss first local var & modified  
#         print(n1,'internal')
#         n1='interna'
#     internal()
#     print(n1)
#     # return n1 #copy value n1
#     # n1=100
# fun()
# print(n1)





# def mysum(n1,n2):#creattion with calling fun &dead with end of function
#     res=n1+n2
#     print(res)#last
# mysum(1,2)
# for numb in range(1,4):
#     print(numb,end=' ')
#     print(numb)
# print('-----')
# print(numb)
#list comprehantion
# logs=[
#     ("server1", "error", "2023-10-01"),
#     ("server2", "info", "2023-10-02"),
#     ("server3", "error", "2023-10-03")
# ]
# #count logs of type error
# #loop on logs &check in log types --->error increment count
# def count(logs):
#     cou=0
#     for l in logs :
#         print(l)
#         if l[1] == "error":
#             cou=cou+1
#     return(cou)
# #extract logs of server_name from all logs
# def extract_logs_for_server(logs, server_name):
#     #list       = [tuple loop logs if log realted to srver name]
#     server_logs = [log for log in logs if log[0] == server_name]  
#     return server_logs
 
# error=count(logs)
# print(f'number of errors is {error}')
# server_name = "server1"
# specific_server_logs = extract_logs_for_server(logs, server_name)
# print(f"Logs for {server_name}: {specific_server_logs}")
# # print(sum(1,2,3,4))
# def count_error_logs(logs):
#      #list comprh. [],(),{}
#      return sum(1 for log in logs if log[1] == "error")

#for --->pass num to if condition---> (true append)
#for --->passs num to append implicity
# l=[num for num in range(1,4) ]
# number=int(input('enter number'))
# largelist=[]
# #generate range from 1 to n+1# r1=range(1,number+1)
# #loop on rangej
# for tablenumber in range(1,number+1):
#     tablelist=[]#clear
#     #genrate range from 1 to 12# r2=
#     #loop on new range
#     for num in range(1,tablenumber+1):
#     #print countwer loop1 * loop2
#         # if(num<=tablenumber):
#         tablelist.append(tablenumber*num)
#         # print(tablenumber*num)
#     largelist.append(tablelist)
# print(largelist)
# #for---> [condition]--->true append
# #for --->append
# largelist2=[[tablenumber*num for num in range(1,tablenumber+1)] for tablenumber in range(1,number+1)]
# print(largelist2)
# l=[]
# for number in range(1,13):
#     if(number%2==0):
#         l.append(number)
# print(l)
# # [valuetoappend loop conditionoptional]
# #for --->condition (true append)
# l2=[number for number in range(1,13) if(number%2==0)]#1,2,,,,12
# print(l2)
# #gernate nummbers even 1 to 12 and append to list
# #list empty
# l=[]
# #loop in range 1,13
# for number in range(1,13):
#     #append number to list
#     # if(number%2==0):
#         l.append(number)
# # #print to list
# print(l)
# # [value loop condition]
# print([number for number in range(1,13) if(number%2==0)])

#functions argument as dict
# def connectotdb (**args):
#     ip=args['ip']
#     username=args['user']
#     passwo=args['p']
#     port=args['port']
#     print(ip,username,passwo,port)
# #call function
# connectotdb(port=3306,ip='192.168.5.20',user='root',p='123')
# print('Date {d} , Message {m}'.format(d='12-12-1200',m='jgkfglfdgjl'))
# #tuple,dict ---->implicity python interp. packing
# #pack values in tuples
# #pack keys*values as dict
# def fun(**kargs):#** type arg is dict
#     print(kargs,type(kargs))
# d={'x':1,'y':2}
# fun(d1=d) #packing {'d1':{'x':1,'y':2}}
# #convert 3 to mutl table (1,2,3)
# number=int(input('enter number'))
# largelist=[]
# #generate range from 1 to n+1# r1=range(1,number+1)
# #loop on range
# for tablenumber in range(1,number+1):
#     tablelist=[]#clear
#     #genrate range from 1 to 12# r2=
#     #loop on new range
#     for num in range(1,tablenumber+1):
#     #print countwer loop1 * loop2
#         # if(num<=tablenumber):
#         tablelist.append(tablenumber*num)
#         # print(tablenumber*num)
#     largelist.append(tablelist)
# print(largelist)