from Videos_Temas.ClaseViedosTema import VideoTema

class MenuVT():

    def menu(self):
        ciclo = 5
        while ciclo > 4:
            print("¿Que desea realizar?")
            print("1.- Agregar\n2.- Eliminar\n3.- Mostrar\n4.- Regresar al Menú")
            rea = int(input(""))
            print("▒" * 50)
            if rea == 1:
                idCurso = input("Proporcione me el Id del curso: ")
                idCT = input("Proporcione me el nombre del tema del curso: ")
                idVideo = input("Proporcione me el nombre del Vídeo: ")                
                agregar = VideoTema(idCurso, idCT, idVideo)
                agregar.agregarInfo()
                print("Se ha agregador la información correctamente")
                print("▒" * 50)
            elif rea == 2:
                print("Estos son los temas que hay")
                archivo = open("./archivos/VT.txt")
                print(archivo.read())
                archivo.close()

                idCurso = input("Por favor, proporcione el id del curso que desea eliminar:\n")
                idCT = input("Por favor, proporcione el id del tema del curso que desea eliminar:\n")
                idVideo = input("Por favor, proporcione el id del video desea eliminar:\n")
                
                eliminar = VideoTema(idCurso, idCT, idVideo)
                eliminar.eliminarInfo()
                
                print(f"Se ha eliminado exitosamente")
                print("▒" * 50)
            elif rea == 3:
                archivo = open("./archivos/VT.txt")
                print(archivo.read())
                archivo.close()
                
                print("▒" * 50)
            elif rea == 4:
                ciclo = 5
        return