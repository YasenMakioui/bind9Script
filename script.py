import os

def validar():
    correcte = True
    while correcte:
        nom = input("Posa el nom del fitxer: ")
        if os.path.isfile("/home/yasin/Desktop/db.{}.com".format(nom)):
            print("El fitxer db.{}.com ja existeix".format(nom))
        else:
            if os.path.isfile("/home/yasin/Desktop/db.local.com"):
                correcte = False
                copyProcess(nom)
            else:
                print("Error: db.local.com no s'ha trobat")
                correcte = False        



def copyProcess(nom):
    if os.path.isfile("/home/yasin/Desktop/db.{}.com".format(nom)):
        print("El fitxer ja existeix")
    else:
        os.system("cp db.local.com db.{}.com".format(nom))
        os.system("sed -i 's/localhost/{}/g' /home/yasin/Desktop/db.{}.com".format(nom))    