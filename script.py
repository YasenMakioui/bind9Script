import os
import sys
import time

def checker():
    bool = True
    while bool:     
        name = sys.argv[1]
        if os.path.isfile("db.{}.com".format(name)):
            print("El fitxer db.{}.com ja existeix".format(name))
        else:
            if os.path.isfile("db.local.com"):
                bool = False
                copyPasteProcess(name)
            else:
                print("Error: db.local.com no s'ha trobat")
                bool = False        


 
def copyPasteProcess(name):
    if os.path.isfile("db.{}.com".format(name)):
        print("El fitxer ja existeix")
    else:
        os.system("cp db.local.com db.{}.com".format(name))
        os.system("sed -i 's/localhost/{}/g' db.{}.com".format(name, name))
        os.system("service bind9 restart")
    
def escribe():
    os.system("echo 'xd'")

def sshConnection():
    os.system('ssh yasin@192.168.1.56 python3 -u - < slave.py')
    
    


#checker()      
sshConnection()