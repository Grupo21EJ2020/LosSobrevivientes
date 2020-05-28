
from Temas.ClaseMenuTemas import MenuTema
from Videos_Temas.ClaseMenuVT import MenuVT
from Empleado.ClaseMenuEmpleados import MenuEmpleado
from Curso.CursoMenu import CursoMenu



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
        MenuEmpleado().menu()
    elif admin == 2:
        CursoMenu().menu()
    elif admin == 3:
        MenuTema().menu()
    elif admin == 6:
        MenuVT().menu()
    elif admin == 7:
        finish = 7