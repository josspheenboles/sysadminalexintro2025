import subprocess
def createuser(username):
    # sudo useradd username
    #homedir -c 
    subprocess.run(['sudo','useradd',username])
    print(f'{username} added')

def removuser(usernam):
    subprocess.run(['sudo','userdel',usernam])
    print(f'{username} deleted')