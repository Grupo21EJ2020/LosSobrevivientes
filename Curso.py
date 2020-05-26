class Curso():
    def __init__(self, idCurso, descripcion, idEmpleado):
        self.__idCurso = idCurso
        self.__descripcion = descripcion
        self.__idEmpleado = idEmpleado

    @property
    def idCurso(self):
        return self.__idCurso

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    def AgregarInformacion(self):
        archivo= open("./archivos/Curso.txt","a",encoding='utf8')
        archivo.write(self.__idCurso +"Cursoinicial" + self.__descripcion + "Matematicas" + self.__idEmpleado + "hola")
        archivo.close()



    