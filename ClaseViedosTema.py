class VideoTema():
    def __init__(self, idCurso, idCT, idVideo):
        self.__idCurso = idCurso
        self.__idCT = idCT
        self.__idVideo = idVideo

    @property
    def idCurso(self):
        return self.__idCurso

    @property
    def idCT(self):
        return self.__idCT

    @property
    def idVideo(self):
        return self.__idVideo
    
    def agregarInfo(self):
        archivo = open("./archivos/VT.txt","a",encoding='utf8')

        archivo.write(self.__idCurso + "|" + self.__idCT + self.__idVideo + "\n")

        archivo.close()

    def eliminarInfo(self):
        archivo = open("./archivos/VT.txt","r",encoding ='utf8')
        guardTemp = []
        for renglon in archivo:
            datos = renglon.split("\n")
            if datos[0] != (self.__idCurso + "|" + self.__idCT + self.__idVideo):
                guardTemp.append(datos[0])
                archivo2 = open("./archivos/VT.txt","w",encoding = "utf8")
                for i in guardTemp:
                    archivo2.write(i + "\n")
                archivo2.close()
        guardTemp.remove()
        archivo.close()
