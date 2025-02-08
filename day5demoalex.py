
##############standred module
import re
regex="[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
#read logs
content=''
with open('/var/log/apache2/error.log','r') as f:
    content=f.read()
print(re.findall(regex,content))
# ips=input('enter ips address')
# regx=r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
# print(re.findall(regx,ips))
# # string with ip
# print(re.match(regx,ip))
# print(re.search(regx,ip))
# print(re.findall(regx,ip))
# if(re.fullmatch(regx,ip) is not None):
#     print('ip is ok')
# # num =input('enternum')
# import sys
# print(sys.argv)

# ip=sys.argv[1]
# port=sys.argv[2]

# import os
# print(os.name)
# if(os.name=='nt'):
#     os.system('dir')
# elif(os.name=='posix'):
#     os.chdir('/')
#     # os.chmod('asd.txt',777)
#     # os.chown('asd.txt',1,1)
#     if(os.getlogin()=='root'):    
#         os.system('touch asd')
# else:
#     print('invalid os')
# import math
# print(math.factorial(5))
# print(math.pi)
# from math import * #call
# print(factorial(5))
#####################################
# from myexper.admin import network
# from myexper import excelfileoperation 
# excelfileoperation.readfromexcel()
# # import excelfileoperation
# import simplefileoperation #accsess all defination inside module
# from simplefileoperation import *
# print(modes)
# print(readfile('asd.txt','all'))
# # import simplefileoperation as sfo
# # print(sfo.modes)
# # content=sfo.readfile('asd.txt','lines')
# # print(content)
# # def writetofile(pathfile,content):
# #     f=open(pathfile,'w')
# #     f.write(content)
#     f.close()
# #object--->class object (instance)

# #read number char,read line ,read lines,read
# def readfile(pathfile,option):
#     print(type(option))
#     f=open(pathfile,'r')
#     if(option=='all'):
#         content= (f.read()) #-----------
#     elif(option=='line'):
#         content=f.readline()
#     elif (option=='lines'):
#         content=f.readlines()
#     #option must be int
#     #isintance(varname,instance type)
#     elif(isinstance(option,int)):
#         content=f.read(option)
#     else:
#         content='invalid option'
#     f.close()
#     return content

# def appendtofile(pathfile,content):
#     f=open(pathfile,'a')
#     f.write(content)
#     f.close()
# #args
# def readwritetofile (pathfile,content=None,option=None):
#     f=open(pathfile,'r+')
#     if(content is not None):
#         f.write(content)
#     elif (option is not None):
#         if(option=='all'):
#             content= (f.read()) #-----------
#         elif(option=='line'):
#             content=f.readline()
#         elif (option=='lines'):
#             content=f.readlines()
#         #option must be int
#         #isintance(varname,instance type)
#         elif(isinstance(option,int)):
#             content=f.read(option)
#         else:
#             content='invalid option'
#     f.close()
#     return content
# def readwritetofile(**args):
#     pass
# readwritetofile(pathfile='asd.txt',option='all')
# readwritetofile(pathfile='asd.txt',content='alljkjkjkjkljkjk')
# # x='5'
# # print(1+x)
# # c=readfile('asd.txt',5)
# # print(c)
# # x=5.5
# # # print(isinstance(x,int))
# # print(type(x))
# # if(type(x)=="<class 'float'>"):
# #     print()
# # print(c.split(' '))
    
# # writetofile('asd.txt','hi sys admin')
# # writetofile('asd2.txt','jhjkhjk')
# # readfile('asd.txt')
# # readfile('asd2.txt')


# ###############################
# # #else for
# # listserver=['ip','ip2']
# # for ip in listserver:
# #     break
# #     print(f'connect server ssh {ip}')
    
# #     #fire run time error 
# # else:
# #     print('all server is ok')
# ######################################################
# #try except
# # # num1=(input('enter number1'))
# # if(num1.isnumeric()):
#     num1=int(num1)
#     num2=(input('enter number2'))
#     if(num2.isnumeric()):
#         num2=int(num2)
#         if(num2!=0):
#             res=(num1/num2)
#             print(res)
#         else:
#             print('cannt divid by zero')
#     else:
#         print('num2 numbers only')
# else:
#     print('num1 numbers only')


# import sys
# answer='y'
# while(answer.lower()=='y'):
#     try:

#         num1=(input('enter number1'))
#         if(num1.isnumeric()):
#             num1=int(num1)
#             num2=(input('enter number2'))
#             if(num2.isnumeric()):
#                 num2=int(num2)
#             else:
#                 print('num2 numbers only')
#         else:
#             print('num1 numbers only')
#         res=(num1/num2)
#     # except ValueError:
#     #     print('numbers only')
#     # except ZeroDivisionError:
#     #     print('cannt divid by zero')
#     except:
#         print(sys.exceptinfo()[1])
#     else:
#          print(f'res={res}')
#     finally:
#         answer=input('enter y to cont. else enter n')
        

# # import sys
# # try:
# #     #write code loop dbs backup
#     #connect backup internent? best try except
#     #1,2,3 bakup done
#     num1=int(input('enter number1'))
#     num2=int(input('enter number2'))
#     print(num1/num2)
    
# except ZeroDivisionError:
#     print('لا يمكن القسمه 0')
# except ValueError:
#     print('numbers only')
# except:#catch parent calss exception
#     # print('call admin')
#     print(sys.exc_info()[1])
# else:
#     print('try done,db backup')
# finally:
#     print('ok')
