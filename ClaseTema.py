class Tema():
    def __init__(self, idTema, nombre):
        self.__idTema = idTema
        self.__nombre = nombre

    @property
    def idTema(self):
        return self.__idTema

    @idTema.setter
    def idTema(self, valor):
        self.__idTema = valor

    @property
    def nombre(self):
        return self.__nombre
    
    def agregarInfo(self):
        archivo = open("./archivos/Temas.txt","a",encoding='utf8')

        archivo.write(self.__idTema + "|" + self.__nombre + "\n")

        archivo.close()

    def eliminarInfo(self):
        archivo = open("./archivos/Temas.txt", "r+")
        for renglon in archivo:
            datos = renglon.split("\n")
            if datos[0] == (self.__idTema + "|" + self.__nombre):
                archivo.write("")
            else:
                print("No existe este dato")
        archivo.close()