#define only functions,class,var
modes=('r','w','r+','a')
def writetofile(pathfile,content):
    f=open(pathfile,'w')
    f.write(content)
    f.close()
#object--->class object (instance)

#read number char,read line ,read lines,read
def readfile(pathfile,option):
    print(type(option))
    f=open(pathfile,'r')
    if(option=='all'):
        content= (f.read()) #-----------
    elif(option=='line'):
        content=f.readline()
    elif (option=='lines'):
        content=f.readlines()
    #option must be int
    #isintance(varname,instance type)
    elif(isinstance(option,int)):
        content=f.read(option)
    else:
        content='invalid option'
    f.close()
    return content

def appendtofile(pathfile,content):
    f=open(pathfile,'a')
    f.write(content)
    f.close()
#args
def readwritetofile (pathfile,content=None,option=None):
    f=open(pathfile,'r+')
    if(content is not None):
        f.write(content)
    elif (option is not None):
        if(option=='all'):
            content= (f.read()) #-----------
        elif(option=='line'):
            content=f.readline()
        elif (option=='lines'):
            content=f.readlines()
        #option must be int
        #isintance(varname,instance type)
        elif(isinstance(option,int)):
            content=f.read(option)
        else:
            content='invalid option'
    f.close()
    return content

