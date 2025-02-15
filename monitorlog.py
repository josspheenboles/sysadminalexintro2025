from mailoperation import *
import re
def monitorlogs(pathlog,reglarepatten):
    f=open(pathlog,'r')
    for line in f:
        if re.search(pattern=reglarepatten,string=line) is not None:
            mysendmail('','',f'{reglarepatten}'+line,'error')
    f.close()