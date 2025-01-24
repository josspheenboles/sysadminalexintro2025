#data types
#STR
#logs 
#Jan 24 08:39:03 jboles-HP-EliteBook-745-G4 systemd[1]: Starting Clean php session files...
log='Jan 24 08:39:03 jboles-HP-EliteBook-745-G4 systemd[1]: Starting Clean php session files...'
#str collectoin of
print(log)
print(log[0],log[1],log[2])
print(log[4:15:1])
print(log[15::1])
print(log[:15:1])
#slicing


# name=input('enter your full name')#fname lname

# print(name.split('a'))#s,r, ,li
# print(name)
#complx
# c1=2+2j
# c2=3+2j
# print(c1,c2,c1+c2,c1-c2)
# print(c1+9)
#numbers--> 1 (int) ,1.1 (float) ,2+2j (complex)
#python2.7 long,python 3.x not long
# num1=10.6
# num2=20.4
# num3=-1
# print(max(num2,num1,num3,100,1000,8000))
# print(min(num2,num1,num3))
# print(round(num1))
# print(round(num2))



# #address --->max int 
# #standred modules
# import sys
# print(sys.maxsize)
# num1=5#--->4b
# num1=9223372036854775807 #long

# print('====>',"" and "go",'===>')#false 

# #arthi + ,* ,/ ,- ,//,**,%
# print(2+3)
# num1=2
# num2=3
# print(num1+num2)#print (2+3)
# print(f'result of sum = num1+num2')
# print(f'result of sum = {num1}+{num2}')
# print(f'result of sum = {num1+num2}')
# print(15/4)
# print(15//4)
# print(9%2)#4,1
# print(2**3)
# operation=input('enter opartion +,-,*,/')
# print(type(num1),type(num2))
# print(num1+num2)#
# # print('dfdf','df',4,5,13.5)
# num1=10
# num2=20
# result=0
# result=num1+num2
# print(result)
#calc

# num1=eval(input('enter number1 '))#datatype str
# num2=eval(input('enter number2'))#datatype str
# result=num1+num2 
# # print(result)
# # result**=2
# # print(result)


# # num1=10
# # num2=10
# # print(num1!=num2) 
# # print(1=='True') #int==str(True) compare value & datatype

# # print(1==True) #int==bool(True) compare value & datatype (True==1)
# # print(2=='2') #int(2)==str(2) #values ok & datatype not ok

# num1=8
# #True and True --->True
# #True and False --->False
# #True and False 
# # print(num1<100 and  num1>9 and num1!=90)
# print(num1<100 or  num1>9 or num1!=90)
# print(not 2)#bool False--->0 True--->1
# print(not 'aya') #not True
# #logical and ,or ,not value not in falsy values
# #False,0,'',"",'''''',"""""",(),[],{}
# print(2 and 5)#True and True 
# #and last True,first false
# #or first true ,last false
# print(() and 5)#False 
# print(() and 5 and 10)