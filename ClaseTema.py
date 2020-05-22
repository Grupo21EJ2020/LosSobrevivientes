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
        archivo = open("./archivos/Temas.txt", "a", encoding="utf8")

        archivo.write(self.__idTema + "|" + self.__nombre)

        archivo.close()

    def eliminarInfo():
        
    def leerInfo():
         archivo = open("./archivos/Temas.txt", "a", encoding="utf8")

         print(archivo.read())

         archivo.close()
         