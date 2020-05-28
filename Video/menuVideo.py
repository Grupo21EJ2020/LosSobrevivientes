from Video import Video

class VideoMenu():
    def menu(self):
        ciclo = 6
        while ciclo > 5:
            print("¿Que necesita realizar?")
            print("1.- Agregar\n, 2.- Eliminar\n, 3.- Modificar\n, 4.-Regresar al menu principal")
            resp = int(input(""))
            print("-" * 50)
            if resp == 1:
                idVideo = input("Inserte el id del Video: ")
                nombre = input("Inserte el nombre del Video: ")  
                url = input("Inserte la url del Video: ")
                fechadepublica = input("Inserte la fecha de publicacion del Video: ")              
                agregar = Video(idVideo,nombre, url, fechadepublica)
                agregar.Agregarvideo()

                print("Se ha agregador la información correctamente")
                print("-" * 50)
            elif resp ==2:
                print("Estos son los Videos excistentes")
                archivo = open("./archivos/Videos.txt")
                print(archivo.read())
                archivo.close()

                idVideo = input("Inserte el id del Video que quiere eliminar: ")
                nombre = input("Inserte el nombre del Video que quiere eliminar: ")  
                url = input("Inserte la url del Video del video que quiere eliminar: ")
                fechadepublica = input("Inserte la fecha de publicacion del Video que quiere eliminar: ")              
                eliminar = Video(idVideo,nombre, url, fechadepublica)
                eliminar.Eliminarvideo()

                print(f"Se ha eliminado el id {idVideo} con el nombre de {nombre} con la url de {url} y la fecha de publicacion de {fechadepublica}")
                print("-" * 50)
            elif resp ==3:
                print("Estos son los Videos excistentes:")
                archivo = open("./archivos/Videos.txt")
                print(archivo.read())
                archivo.close()      

                idVideo = input("Inserte el id que queire modificar: ")
                nombre = input("Inserte el nombre del Video que queire modificar: ")  
                url = input("Inserte la url del Video que quiere modificar: ")
                fechadepublica = input("Inserte la fecha de publicacion del Video que quiere modificar: ")              
                modificar = Video(idVideo,nombre, url, fechadepublica)
                modificar.modificarInfo()          

                print("-" * 50)
            elif resp ==4:
                archivo = open("./archivos/Videos.txt")
                print(archivo.read())
                archivo.close()
                
                print("-" * 50)
            elif resp ==5:
                ciclo = 5
        return

        