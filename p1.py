
ban =True
while ban:
    opc = int(input("Menú\n1)Crear lista\n2)Añadir elemento\n3)Eliminar un elemento\n4)Modificar elemento\n"
                    "5)Mostrar datos\n6)Mostrar datos de forma inversa\n7)Limpiar lista\n8)Borrar lista\n9)Cerrar\n¿Que opcion prefiers?  "))
    if(opc == 1):
        lista= []
        print(f"Lista Creada\n {lista}")
        
    elif(opc == 2):
        lista.append(input("Valor del elemento: "))
        print(f"{lista}\n+{len(lista)}")
    elif(opc == 3):
        print(lista)
        pos = int(input("Que posicion quieres eliminar(Recuerda que empezamos a cortar desde 0: "))
        if pos >=0 and pos <= len(lista):
            lista.pop(pos)
        else:
            print("Error de posicion")
    elif(opc == 4):
        print(lista)
        pos = int(input("Que posicion quieres modificar(Recuerda que empezamos a cortar desde 0: "))
        if pos >=0 and pos <= len(lista):
            new = input("Nuevo valor: ")
            lista[pos]=new
        else:
            print("Error de posicion")
    elif(opc == 5):
        print(f"Datos:\n{lista}")
    elif(opc == 6):
        reversa=[]
        for x in lista[::-1]:
            reversa.append(x)
        print(f"Reversa:\n {reversa}")
    elif(opc == 7):
        print(lista)
        lista.clear()
        print(f"Lista limpia\n{lista}")
    elif(opc == 8):
        print("Lista borrada")
    elif(opc == 9):
        ban=False
    else:
        print("Error de opcion")
print("Adios")