import excel
excel.read('asd.xlsx',1,1)
p=input('enter excel par')
excel.read(p,2,2)

#write to excel file
# import openpyxl
# #open exs. fill
# wb=openpyxl.load_workbook('asd.xlsx')
# for name in wb.sheetnames:
#     sheet=wb[name]
#     for row in sheet.iter_rows():
#         for col in row:
#             print('col value')
# sheet=wb.active
# print(sheet['A1'].value)
# sheet['A2']='dsdsd'
# wb.save('asd.xlsx')
# #create workbook
# wb=openpyxl.Workbook()
# #define sheet
# sheet=wb['ui ux']
# # sheet=wb.active
# sheet['C6']='python'
# sheet.cells(3,6)='bash'
# print(sheet['C6'].value)
# print(sheet.cells(3,6).value)
# wb.save('asd.xlsx')
#simple file (file can open with notpad)
# open('asd.xlsx','r')

####overloading
# def mysum(x,y):#2 arg
#     print(x+y)
# def mysum(x,y,z=0): # 3 arg 
#     print(x+y+z)
# def mysum(*args):
#     res=0
#     for n in args:
#         res+=n

# mysum(1,2,3)
# mysum(1,2)
# print(mysum)
# def sum(int x,int y):
#     pass
# def sum(float x,float y):
#     pass

###########################################
# from Human import *

# aya=Human(1,'ayya') 
# aya.bd='24-1-200'
# # 
# aya.count=1000
# # print(aya.bd)
# mai=Human(2,'mai','F')
# # print(mai.bd)
# print(aya.count,Human.count)
# mark=Human(3,'mark','M')
# print(mai.count,Human.count)

# # aya.name='aya'
# # print(aya.id,aya.name)
# # print(mai.id,mai.name)
# # print(mark.id,mark.name)
# # mai=Student()
# # print(mai,type(mai))