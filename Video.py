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

    def Agregar_video(self):
        archivo = open("./archivos/Videos.txt", encoding="utf8")

        archivo.write(self.__idVideo + "|" + self.__nombre + "|" + self.__url + "|" + self.__fechapublicacion)

        archivo.close()
