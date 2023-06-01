
dispositivos=[]
quieres_continuar="S"



while quieres_continuar=="S" or quieres_continuar=="SI":
    print("---------Menu---------")
    print("1. Ingresar dispositivo")
    print("2. Mostrar dispositivo")
    print("3. Modificar dispositivo")
    print("4. Mostrar todos los dispositivos")
    print("5. Eliminar dispositivo")
    print("6. Salir")
    opcion=input("Ingrese una opción: ")
    if opcion.isalpha():
        print("Debes ingresar una opción: del 1 al 6 ")
        quieres_continuar="S"
    elif opcion.isdigit():
        if opcion=="1":
            nombre=input("Ingrese el nombre del dispositivo: ")
            if not nombre:
                print("El nombre no puede estar vacio")
                opcion="1"
            elif nombre in dispositivos==True:
                print("Este dispositivo ya existe")
            else:
                dispositivos.append(nombre.upper().strip())
                print("Dispositivo insertado")
                print(dispositivos)
                quieres_continuar=input("Quieres realizar otra operación? (S/N): ")

                if quieres_continuar.isnumeric():
                    quieres_continuar="S"
                else:
                    quieres_continuar = quieres_continuar.upper()

        elif opcion=="2":
            nombre = input("Ingrese el dispositivo a buscar:").upper().strip()
            print(dispositivos)
            if nombre in dispositivos == True:
                for dispositivo in range(len(dispositivos)):
                    if dispositivos[dispositivo]==nombre:
                        print(dispositivos[dispositivo])
            elif nombre in dispositivos==False:
                print("Este dispositivo no existe")
            else:
                for dispositivo in range(len(dispositivos)):
                    print(dispositivos[dispositivo])
        elif opcion=="3":
            nombre = input("Ingrese el dispositivo a modificar: ").upper().strip()
            for dispositivo in range(len(dispositivos)):
                if dispositivos[dispositivo] == nombre:
                    dispositivos[dispositivo]=input("Ingrese el nuevo nombre del dispositivo: ").upper().strip()
                    print("El dispositivo se ha modificado correctamente")
                    opcion="4"
                else:
                    print("El nombre que ingresó no se encuentra en la lista")
                    opcion="3"
        elif opcion=="4":
            for dispositivo in range(len(dispositivos)):
                print(dispositivos[dispositivo])
        elif opcion=="5":
            nombre = input("Ingrese el dispositivo a eliminar: ").upper().strip()
            for dispositivo in range(len(dispositivos)):
                dispositivos.remove(dispositivos[dispositivo])
            print("El dispositivo se ha modificado correctament")
        elif opcion=="6":
            quieres_continuar="N"
    else:
        quieres_continuar="S"

