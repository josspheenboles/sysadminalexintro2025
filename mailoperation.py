import smtplib
import socket

def mysendmail(sender,reciver,msg,subject):
    #create object from SMTP
    servermail=smtplib.SMTP('smtp@com1.com')
    try:
        servermail.sendmail(sendermail,receivermail,msg=msg,subject=subject)
    except socket.gaierror:
        print('invalid emaill address,connection issue')
