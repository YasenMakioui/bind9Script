import os
import sys

def validar():
    correcte = True
    while correcte:     
        nombre = sys.argv[1]
        print("db.{}.com".format(nombre))
        if os.path.isfile("db.{}.com".format(nombre)):
            print("El fitxer db.{}.com ja existeix".format(nombre))
        else:
            if os.path.isfile("db.local.com"):
                correcte = False
                copyProcess(nombre)
            else:
                print("Error: db.local.com no s'ha trobat")
                correcte = False        



def copyProcess(nombre):
    if os.path.isfile("db.{}.com".format(nombre)):
        print("El fitxer ja existeix")
    else:
        os.system("cp db.local.com db.{}.com".format(nombre))
        os.system("sed -i 's/localhost/{}/g' db.{}.com".format(nombre, nombre))    



validar()      

