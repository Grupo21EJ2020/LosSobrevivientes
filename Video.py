class Video:
    def __init__(self, idVideo, nombre, url, fechapublicacion):
        self.__idVideo = idVideo 
        self.__nombre = nombre
        self.__url = url
        self.__fechapublicacion = fechapublicacion

    #Propiedades
    @property
    def idVideo(self):
        return self.__idVideo
    
    @idVideo.setter
    def idVideo(self, valor):
        self.__idVideo = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, valor):
        self.__url = valor

    @property
    def fechapublicacion(self):
        return self.__fechapublicacion
    
    @fechapublicacion.setter
    def fechapublicacion(self, valor):
        self.__fechapublicacion = valor
    
    #Metodos de instancia

    def ImprimirTodo(self):
        archivo = open("./archivos/Videos.txt", encoding="utf8")

        print(archivo.read())

        archivo.close()

    def Agregarvideo(self):
        archivo = open("./archivos/Videos.txt", encoding="utf8")

        archivo.write(self.__idVideo + "|" + self.__nombre + "|" + self.__url + "|" + self.__fechapublicacion + "\n")

        archivo.close()
    
    def Eliminarvideo(self):
        archivo = open("./archivos/Videos.txt", "r", encoding="utf8")
        listdelete = []
        for linea in archivo:
            info = linea.split("\n")
             if info[0] != (self.__idVideo + "|" + self.__nombre + "|" + self.__url + "|" + self.__fechapublicacion):
                listdelete.append(info[0])
                archivo2 = open("./archivos/Videos.txt", "w", encoding = "utf8")
                for a in listdelete:
                    archivo2.write(a + "\n")
                archivo2.close()
        listdelete.remove()
        archivo.close()