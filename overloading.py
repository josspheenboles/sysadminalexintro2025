import multipledispatch
from multipledispatch import dispatch
@dispatch(int,int)
def add(x,y):
    print(type(x),type(y))
@dispatch(float,int)
def add(x,y):
    print(type(x),type(y))
@dispatch(int,int,int)
def add(x,y,z):
    print(type(x),type(y),type(z))
add(1,2)
add(1,2,3.3)
add(1.1,2)
# #add (int,int)
# #add (int,int,int)
# #add (float,float)
# #add (int,float)
# # def add(x,y,z=0):
# #     print (x+y+z)

# # add(1,2)
# # add(1,2,3)
# def add(datatype,*args):
#     if(isinstance(args[0],int) or isinstance(args[0],float) ):
#         res=0
#         for number in args:
#             res+=number
#         print(res)
#     elif (isinstance(args[0],str)):
#         res=''
#         for number in args:
#             res+=number
#         print(res)
#     else:
#         print('invalid data type')

# add(1)
# add(1,2)
# add(1,2,3)
# add(1,2,3,4)