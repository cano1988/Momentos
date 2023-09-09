# Vamos a crear un diccionario con los colores

colores={}


ingreso= int(input("Desea ingresar, editar o eliminar un color\n1.Ingresar \n2.Editar \n3.Eliminar \n4.Salir \n"))

while ingreso == 1:

    llaves=input("ingrese clave del color: ")
    valores=input("Ingrese color: ")
    colores.update({llaves:valores})
    print(colores)
    ingreso= int(input("Desea ingresar, editar o eliminar un color\n1.Ingresar \n2.Editar \n3.Eliminar \n4.Salir \n"))
while ingreso ==2:
    llaves=input("ingrese clave del color: ")
    valores=input("Ingrese color: ")
    colores.update({llaves:valores})
    print(colores)
    ingreso= int(input("Desea ingresar, editar o eliminar un color\n1.Ingresar \n2.Editar \n3.Eliminar \n4.Salir \n"))
while ingreso ==3:
    llaves=input("ingrese clave del color: ")
    colores.pop(llaves)
    print(colores)
    ingreso= int(input("Desea ingresar, editar o eliminar un color\n1.Ingresar \n2.Editar \n3.Eliminar \n4.Salir \n"))
while ingreso ==4:
    break
while ingreso <0 or ingreso >4:
    print  ("Opción invalida")
    ingreso= int(input("Desea ingresar, editar o eliminar un color\n1.Ingresar \n2.Editar \n3.Eliminar \n4.Salir \n"))
