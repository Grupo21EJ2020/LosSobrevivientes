from ClaseMenuTemas import MenuTema
from ClaseMenuVT import MenuVT
from CursoMenu import CursoMenu


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
            print("1.Agregar Info\n 2.Borrar Info\n 3.Modificar info\n 4.Consultar Info\n 5.Ver detalles especificos\n 6.Regresar al menu" )
            opcion = int(input(""))

            if opcion == 6:
                print ("Regresaras al menu principal ")


    elif admin ==2:
        CursoMenu().menu
    elif admin == 3:
        MenuTema().menu()
    elif admin == 6:
        MenuVT().menu()
    elif admin == 7:
        finish = 7