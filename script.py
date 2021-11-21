import os

def validar():
    correcte = True
    while correcte:
        path = ""
        nom = input("Posa el nom del fitxer: ")
        directori = input("Indica la ruta, si estas executant el script a la mateixa carpeta on vols realitzar el process, posa \"Aqui\"")
        if not directori == "Aqui":
            path = directori + "/"         
        

        if os.path.isfile("{}db.{}.com".format(path, nom)):
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