#function formate 
#dict collection of values diff datatype,
#pairs (key , value)
#keys unique & as string
d={
# 'id':1,
'Name':'aya ali',
'track':'sys admin',
'courses':['oop','bash','admin'],
'grades':(100,99,99.5),
'id':100 #update value of key id
}
# + concat * mult
d2={'id':1000,'branch':'alex'}
d.update(d2)#overwrite value in d2 on d
print(d)
print(d2)

# print(d+d2)#unique key
# print(d*3)#d--->d
# for key,value in d.items():
#     print(key,value)
    # print(item[0],item[1])
# for value in d.values():
#     print(value)
# for key in d:
#     print(key,d[key],type(d[key]))
# d['x']='xccc'
# # d['id']=1000
# print(d,type(d))
# print(d['track'])
#function

# min(1,4,6,7)
# def myfun(*arg):#as arg  tuple
#     print(arg,type(arg))
# x,y,z=1,2,3 #unpacking
# myfun(x,y,z)#separted values --->packing in tuple 
# # # range([start],end,[step])#
# '{date}'.format(date='1-1-2000')
# #default arg ,non default arg --->default arg
# def myfun(y,z=0,x=1):
#     print(z,y,x)
# myfun(1,3,5)
# myfun(1,3)
# myfun(1)
# range(1,13,1)
# range(1,13)
# range(13)#0--->1
# # # input no out
# # def mysum(num1,num2):
# #     return (num1+num2)
# # #calling
# # print(mysum(3,2))
# # var=mysum(1,5)
# print(var,var+9)
# print(mysum(9,8))
# sre2=input('jhjkhk')
# print('hkkkh')
# 'lklk'.isdigit()--->t,f
# l=[1,2,3]
# for n in l:
#     print(n)
# #tips trickes
# print(print('hi sys '))
# print('hi sys '.isdigit())
# l=[2,3]
# print(l.append('pkppk'))
# print(l.pop(0)) #input

# # count vars=count tuple items
# *z,x,y=(1,2,3,3,4,7,7)
# print(z,x,y)
# l=['one',1,True]
# for index,item in enumerate(l):#index,item=(0,'one')
#     print(f'item: {item},index:{index}')
# # t=2,1.1,True,(),[],{},'dffd'
# # print(type(t))
# #declare mul. variab
# #unpacking
# # x,y,z=a
# # t=(1,1.1,'fff')
# # x,y,z=t
# # print(x,y,z)
# name='aya ali'
# index=0
# for char in name:
#     print(char,index)
#     index+=1
# print(enumerate(name)) #(index,value),()...()
# for char,index in enumerate(name):
#     print(f'Char : {char},index: {index}')
#     # print(f'Char : {t[0]},index: {t[1]}')
# # #data structue
# l=[]
# l2=l.copy()#address l =address l2
# l.append('pllapal')
# # l2.append('c')
# print(l,l2)
#tuple collection of values diff data type,hetr.,not fiexd size,immutable list
#t=(1,1.1,True,'one',[],(),{})
# t=list(t)#address
# # t.append('plplp')
# # t=tuple(t)
# print(t)
# #create list [1,3]--->new address
# # t[4]=[1,3]
# print(t)
# t[4].append(1)
# t[4].append(3)
# print(t)

# t[0]=199
# print(t,type(t))
# print(t[1:4])
# print(len(t))
# print(t[::-1])
# print(True==1) #check value & datatype
# print(True==2)
# print(True and 2) #check is 2 one of the falsy value

# True==1 #check only value,
# False==0
# l=[True,1]
# for item in l:
#     if(item==1):#True==1
#         print('reomve')
# l.remove(1)#reomve only one item
# print(l) #
#data structure
#data types int ,.....
#array collection of values same data type,storing in memeory cont,fixed size
#arr --->int 10 --->40 b
# adminskils=['admin1','admin2','ccna']
# progskils=['bash','python']
# print(adminskils*2)
# skils=adminskils+progskils

# print(adminskils+progskils)#on the fly
# print(adminskils)
# print(progskils)
# print(adminskils*2)
# skils=[]
# print(skils)
# skils.extend(adminskils)
# print(skils)
# skils.extend(progskils)
# print(skils)
# print(adminskils+progskils)
# print(progskils,adminskils)
#list collection of values diff data type,hetr.,not fiexd size
# l=[1, 2.2,True,'one',[],(),{},'one']
# # l.pop(3)
# if('one1' in l):
#     l.remove('one1')
# # for item in l:
# #     if(item=='one1'):        
# #         l.remove('one1')
# # l.pop()
# # l.pop()
# l.pop()
# l.pop()
# l.pop()
# l.pop()
# l.pop()
# print(l)
# l[0]=199
# # l[7]=89
# l.append('plplplp--->end')
# l.insert(0,'plplpl')
# print(l)
# for item in l:
#     print(item,type(item))
# print(l[::-1])
# print(l[1:5])
# print(l[0],len(l))
# print(l[7])
# print(l,type(l))
# for n in range(1,2):
#     pass
# #while loop until condition
# #flag 
# flag=True
# #while (flag is ok)
# while flag==True:
#     #input names 
#     name =input('enter name')
#     #ask do you enter another name
#     answer=input('enter y to cont. n for exsit')
#     #if ok cont
#     #Y=='y'
#     # if(answer.lower()=='y'):
#     if(answer=='y' or answer=='Y'):
#         flag=True
#     #else change flag to not ok
#     else:
#         flag=False
#         # exit()
# print('after exit')

# #10 server
# for  num in range(1,13): #12 loop
#    if(num==3): #1,2,3break,...,12
#        continue
# else:
#     print('all server are backuped')

# ip=input('enter ip')
# count=0
# for char in ip:
#     if(not char=='.'):
#         continue
#     count+=1
    
# r=range(1,13) #[1,..12]
# #break,contin.
# for month in r:
#     if(month==7):
#         continue #only break loop 7
#         # break #break loop
#     print(month)
# # #define inputs ['aya',"sara"]
# # #----> #define output aya \n sara
# # #input names
# # names=input('enter names')
# # #remove [,],'',""
# # names=(names.replace(']','')).replace('[','')

# # #loop in names 
# #     #print each names


# names=input("enter names separated with [name1,name2,...]")
# names=names.replace('"','').replace("'","").replace(']','').replace('[','')
# names=names.split(',')
# for name in names:
#     print(name)


# 
# # #all ok
# # #string check no. [],'',""
# # #['aya',"sara"]
# # #aya
# # #sara
# # names=(input('enter names [name1,name2,...]'))
# # names=names.replace(']','').replace('[','').replace('"','').replace("'",'')
# # names=names.replace(',','\n')
# # print(names)
# # print(names.split(','))
# # for name in names.split(','):
# #     print(name)
# # print(type(names),names)
# # # print(names[1:len(names)-1:1]) #ok

# # # names=names.split(' ')
# # # newstr=''
# # for char in names:
# #     if(char.isalpha()):
# #         newstr+=char
# #     elif(char==','):
# #         newstr+=char
# print(newstr.split(','))
