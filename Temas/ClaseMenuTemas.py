from Temas.ClaseTema import Tema

class MenuTema():

    def menu(self):
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
                print("▒" * 50)
            elif rea == 3:
                print("Estos son los temas que hay")
                archivo = open("./archivos/Temas.txt")
                print(archivo.read())
                archivo.close()                
                
                idTema = input("¿Cúal id desea modificar?\n ")
                nombre = input("¿Cómo desea renombrarlo?\n ")

                modi = Tema(idTema, nombre)
                modi.cambiarInfo()
                
                print("▒" * 50)
            elif rea == 4:
                archivo = open("./archivos/Temas.txt")
                print(archivo.read())
                archivo.close()
                
                print("▒" * 50)
            elif rea == 5:
                ciclo = 5
        return