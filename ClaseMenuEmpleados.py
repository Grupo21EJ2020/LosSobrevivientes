from ClaseEmpleado import Empleado

class MenuEmpleado():

    def menu(self): 
        opcion = 0
        while opcion < 6 :
            print ("¿Que accion se desea realizar?")
            print("1.Agregar Info\n 2.Borrar Info\n 3.Modificar info\n 4.Consultar Info\n 5.Ver detalles especificos\n 6.Regresar al menu" )
            opcion = int(input("Elige una opcion: "))
            print ("*" * 20)
            if opcion == 1:
                idEmpleado = input("Ingrese el Id del Empleado: ")
                nombre = input("Ingrese el nombre del Empleado: ")   
                direccion = input("Ingrese la direccion del Empleado: ")
                agregar = Empleado(idEmpleado, nombre, direccion)
                agregar.agregarInfo()           
   
                print("Se ha agregador la información correctamente")
                print("*" * 20)

            elif opcion == 6:
                print ("Regresaras al menu principal ")
             