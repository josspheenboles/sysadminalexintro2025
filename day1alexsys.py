# # # print('hi sys alex')
# # # names='aya ali' #single os string
# # names='''aya ali
# # mai ahmed''' #multi line
# # datatype varname[=value] ;
# # varname=value #detected datatype
# #loosly typed,dynamic
# x=10
# print(type(x))
# x=10.2
# print(type(x))
# x=True
# print(type(x))
# x='aya ali'
# print(type(x))
# x=()
# print(type(x))
# x=[]
# print(type(x))
# x={}
# # print(type(x))
# age=input('enter  age')
# #casintng
# age=int(age)
# print(type(age))
age=eval(input('enter age')) #auto detect datatype--->auto cast 2.2
print(type(age))