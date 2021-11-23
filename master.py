import os
import sys
import time

def checker():
    bool = True
    while bool:     
        name = sys.argv[1]
        if os.path.isfile(f"db.{name}.com"):
            print("El fitxer db.{name}.com ja existeix")
        else:
            if os.path.isfile("db.local.com"):
                bool = False
                copyPasteProcess(name)
            else:
                print("Error: db.local.com no s'ha trobat")
                bool = False        


 
def copyPasteProcess(name):
    #configurar el archivo db
    if os.path.isfile(f"db.{name}.com"):
        print("El fitxer ja existeix")
    else:
        os.system(f"cp db.local.com db.{name}.com")
        os.system(f"sed -i 's/localhost/{name}/g' db.{name}.com")
        zoneConfig(name)
    
def sshConnection():
    os.system(f'ssh yasin@{sys.argv[1]}')

def zoneConfig(name):
    #configurar la zona
    f = open("named.conf.local", "a")
    f.write('zone "{}.com" { type master; file /etc/bind/db.{name}.com; allow-transfer {sys.argv[1]};  }'.format(name))
    f.close()


if __name__ == '__main__':
    checker()
    #sshConnection()