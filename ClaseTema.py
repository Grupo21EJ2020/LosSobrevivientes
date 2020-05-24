class Tema():
    def __init__(self, idTema, nombre):
        self.__idTema = idTema
        self.__nombre = nombre

    @property
    def idTema(self):
        return self.__idTema

    @property
    def nombre(self):
        return self.__nombre
    
    def agregarInfo(self):
        archivo = open("./archivos/Temas.txt","a",encoding='utf8')

        archivo.write(self.__idTema + "|" + self.__nombre + "\n")

        archivo.close()

    def eliminarInfo(self):
        archivo = open("./archivos/Temas.txt","r",encoding ='utf8')
        guardTemp = []
        for renglon in archivo:
            datos = renglon.split("\n")
            if datos[0] != (self.__idTema + "|" + self.__nombre):
                guardTemp.append(datos[0])
                archivo2 = open("./archivos/Temas.txt","w",encoding = "utf8")
                for i in guardTemp:
                    archivo2.write(i + "\n")
                archivo2.close()
        archivo.close()