from Curso import Curso

class CursoMenu():
    def menu(self):
        ciclo = 6
        while ciclo > 5:
            print("¿Que necesita realizar?")
            print("1.- Agregar\n, 2.- Eliminar\n, 3.- Modificar\n, 4.-Regresar al menu principal")
            resp = int(input(""))
            print("▒" * 50)
            if resp == 1:
                idCurso = input("Inserte el id del Curso: ")
                descripcion = input("Inserte la descripcion del Curso: ")  
                idEmpleado = input("Insete el id del Empleado: ")              
                agregar = Curso(idCurso,descripcion, idEmpleado)
                agregar.agregarInfo()

                print("Se ha agregador la información correctamente")
                print("▒" * 50)
            elif resp ==2:
                print("Estos son los Cursos que estan disponibles")
                archivo = open("./archivos/Cursos.txt")
                print(archivo.read())
                archivo.close()

                idCurso = input("Inserte el id del Curso que desee Eliminar:\n")
                descripcion = input("Inserte la descripcion que desee Eliminar:\n")
                idEmpleado = input("Inserte el id del Empleado que desee Eliminar:\n")

                eliminar = Curso(idCurso,descripcion, idEmpleado)
                eliminar.eliminarInfo()

                print(f"Se ha eliminado el id {idCurso} con la descripcion {descripcion} y con el numero de Empleado {idEmpleado}")
                print("▒" * 50)
            elif resp ==3:
                print("Estos son los Cursos disponibles:")
                archivo = open("./archivos/Cursos.txt")
                print(archivo.read())
                archivo.close()                
                
                idCurso = input("¿Cúal id desea modificar?\n ")
                descripcion = input("¿Como desea cambiar la descripcion?\n ")
                idEmpleado = input("¿Cual id desea modificar?")

                modi = Curso(idCurso, descripcion, idEmpleado)
                modi.cambiarInfo()
                
                print("▒" * 50)
            elif resp ==4:
                archivo = open("./archivos/Cursos.txt")
                print(archivo.read())
                archivo.close()
                
                print("▒" * 50)
            elif resp ==5:
                ciclo = 5
        return

        

               
                
