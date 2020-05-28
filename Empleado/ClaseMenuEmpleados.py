from Empleado.ClaseEmpleado import Empleado

class MenuEmpleado():

    def menu(self): 
        opcion = 0
        while opcion < 5 :
            print ("¿Que accion se desea realizar?")
            print(" 1.Agregar Info\n 2.Borrar Info\n 3.Modificar info\n 4.Consultar Info\n 5.Regresar al menu" )
            opcion = int(input("Elige una opcion: "))
            print ("*" * 20)

            if opcion == 1:
                print ("A seleccionado agregar informacion \n ")
                idEmpleado = input("Ingrese el Id del Empleado: ")
                nombre = input("Ingrese el nombre del Empleado: ")   
                direccion = input("Ingrese la direccion del Empleado: ")
                agregar = Empleado(idEmpleado, nombre, direccion)
                agregar.agregarInfo()           
   
                print("Se ha agregador la información correctamente")
                print("*" * 20)

            elif opcion == 2:
                print ("A seleccionado borrar informacion \n ")
                print("Estos son los Empleados registrados")
                archivo = open("./archivos/Empleados.txt")
                print(archivo.read())
                archivo.close()

                idEmpleado = input("Ingrese el id del Empleado que desea eliminar: ")
                nombre = input("Ingrese el nombre del empleado a eliminar: ")
                direccion =input("Ingrese la direccion a eliminar: ")
                borrar =  Empleado(idEmpleado, nombre, direccion)
                borrar.borrarInfo()
                print(f"Se ha eliminado el empleado con id {idEmpleado}, nombre {nombre} y direccion: {direccion} ")
                print("*" * 50)

            elif opcion == 3:
                print ("A seleccionado modificar informacion \n ")
                print("Empleados registrados:")
                archivo = open("./archivos/Empleados.txt")
                print(archivo.read())
                archivo.close()                
                
                idEmpleado = input("¿Cúal id de empleado desea modificar?:  ")
                nombre = input("Nombre a modificar: ")
                direccion = input("Direccion a modificar: ")

                modificaciones = Empleado(idEmpleado, nombre, direccion)
                modificaciones.modificarInfo()
                
                print("*" * 20)
                    

            elif opcion == 4:
               print ("A seleccionado ver el registro de los empleados \n ")
               archivo = open("./Archivos/Empleados.txt")
               print(archivo.read())
               archivo.close()

               print("*" * 20)
   

            elif opcion == 5:
                break 

     
             