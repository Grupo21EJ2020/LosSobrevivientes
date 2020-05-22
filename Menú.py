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

    #if admin == 1:

    if admin == 3:
        ciclo = 6
        while ciclo > 5:
            print("¿Que desea realizar?")
            print("1.- Agregar\n2.- Eliminar\n3.- Modificar\n4.- Mostrar\n5.- Regresar al Menú")
            rea = int(input(""))
            print("▒" * 50)
            if rea == 1:
                idTema = int(input("Proporcione me el Id del tema: "))
                nombre = input("Proporcione me el nombre del tema: ")
                agregar = Tema(idTema, nombre)
                print("Se ha agregador la información correctamente")
                print("▒" * 50)
            elif rea == 4:
                archivo = open("./archivos/Temas.txt", "r", encoding="utf8")
                for x in archivo:
                    datos = x.split("|")
                    print("idTema", datos[0])
                    print("Nombre", datos[1])
                archivo.close()
                print("▒" * 50)
            elif rea == 5:
                ciclo = 5

    elif admin == 7:
        finish = 7