import shutil
import mailoperation
import os
import time

sendermail='asd2@com1.com'
receivermail='asd@com1.com'
subject='test mail'

def cleanup(path,dayscount):
    nowtime=time.time()
    for file in os.listdir(path=path):
        # filepath='/var/log/'+file
        filepath=os.path.join(path,file)
        if(os.path.isfile(filepath)):
            fileage=nowtime-os.path.getmtime(filepath)
            if(fileage>dayscount*86400):
                os.remove(filepath)
                print(f'{filepath} deleted')


def copydirs(listsourcedirs,listdestination):
    if len(listsourcedirs) ==len(listdestination):
        for index,dir in enumerate(listsourcedirs):
            copydirectory(dir,listdestination[index])
    else:
        return 'copying stopped count of source must = des.'
def copydirectory(sourcepath,destnationpath):
    if(os.path.isdir(sourcepath) and os.path.isdir(destnationpath)):
        shutil.copytree(sourcepath,destnationpath)
def checkdiskuusage(path,percenrage):
    usage=shutil.disk_usage(path=path)#static path
    percentusage=(usage.used/usage.total)*100
    if(percentusage>percenrage):#static percentage
        msg=f'disk {path} used up to {percentusage}'
        mailoperation.mysendmail(sender=sendermail,reciver=receivermail,msg=msg,subject=subject)

# print(type(usage))