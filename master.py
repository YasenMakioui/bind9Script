import os
import sys
import time

def options():
    print("Que vols fer:")
    option = input("1 - Configuració inicial master i slave\n2 - Afegir un domini nou a un bind ja configurat\n")
    if option == "1":
        print("opcion 1")
    elif option == "2":
        print("opcion 2")
    else:
        print("mal")        

def checker():
    bool = True
    while bool:     
        name = sys.argv[1]
        if os.path.isfile(f"db.{name}.com"):
            print(f"El fitxer db.{name}.com ja existeix")
            bool = False
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
    zone = ['',f'zone "{name}.com"' + '{', '\ttype master;', f'\tfile /etc/bind/db.{name}.com;',f'\tallow-transfer '+ '{ ' + sys.argv[2] + '; };', '}']
    with open("named.conf.local", "a") as f:
        f.writelines('\n'.join(zone))
        f.close()

def systemRestart():
    time.sleep(3)
    os.system("service bind9 reload")

if __name__ == '__main__':
    #checker()
    #sshConnection()
    #systemRestart()
    options()