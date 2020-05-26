from ClaseTema import Tema

finish = 8
while finish > 7:

    print("Bienvenido ¿Qué es lo que desea hacer?")
    print("1.- Administrar los Empleados\n2.- Administrar Cursos\n" 
        "3.- Administrar Temas\n4.- Administrar Videos\n"
        "5.- Administar Temas Asignados al Curso\n6.- Administrar Videos Asignados al Tema\n"
        "7.- Salir"
        )
    admin = int(input(""))
    print("▒" * 50)

    
    if admin == 1:
        opcion = 0
        while opcion < 6 :
            print ("¿Que accion se desea realizar?")
            print("1.Agregar Info\n 2.Borrar Info\n 3.Modificar info\n 4.Consultar Info\n 5.Ver detalles especificos\ 6.Regresar al menu" )
            opcion = int(input(""))

            if opcion == 6:
                print ("Regresaras al menu principal ")
            


    if admin == 3:
        ciclo = 6
        while ciclo > 5:
            print("¿Que desea realizar?")
            print("1.- Agregar\n2.- Eliminar\n3.- Modificar\n4.- Mostrar\n5.- Regresar al Menú")
            rea = int(input(""))
            print("▒" * 50)
            if rea == 1:
                idTema = input("Proporcione me el Id del tema: ")
                nombre = input("Proporcione me el nombre del tema: ")                
                agregar = Tema(idTema, nombre)
                agregar.agregarInfo()
                print("Se ha agregador la información correctamente")
                print("▒" * 50)
            elif rea == 2:
                print("Estos son los temas que hay")
                archivo = open("./archivos/Temas.txt")
                print(archivo.read())
                archivo.close()

                idTema = input("Por favor, proporcione el id del tema que desea eliminar:\n")
                nombre = input("Por favor, proporcione el nombre del tema que desea eliminar:\n")
                eliminar = Tema(idTema, nombre)
                eliminar.eliminarInfo()
                print(f"Se ha eliminado el id {idTema} con el nombre {nombre}")
            elif rea == 4:
                archivo = open("./archivos/Temas.txt")
                print(archivo.read())
                archivo.close()
                print("▒" * 50)
            elif rea == 5:
                ciclo = 5

    elif admin == 7:
        finish = 7