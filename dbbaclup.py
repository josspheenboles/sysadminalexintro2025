import subprocess
dbname='iti'
desnationpath='/home'
username='root'
password='123'
def backup(dbmscmd,dbname,desnationpath,usename,password):
    subprocess.run(['sudo',dbmscmd,'-u',username,'-p',password,dbname,
                    '>',desnationpath+'/'+dbname+'.sql'])
    print(f'database backuped in {desnationpath}/{dbname}.sql')

