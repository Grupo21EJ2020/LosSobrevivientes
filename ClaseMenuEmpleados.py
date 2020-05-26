from ClaseEmpleado import Empleado

class MenuEmpleado():

    def menu(self): 
        opcion = 0
        while opcion < 6 :
            print ("¿Que accion se desea realizar?")
            print("1.Agregar Info\n 2.Borrar Info\n 3.Modificar info\n 4.Consultar Info\n 5.Ver detalles especificos\n 6.Regresar al menu" )
            opcion = int(input(""))

            if opcion == 6:
                print ("Regresaras al menu principal ")
        return        