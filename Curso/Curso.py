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

    def agregarInfo(self):
        archivo = open("./archivos/Cursos.txt","a",encoding='utf8')

        archivo.write(self.__idCurso + "|" + self.__descripcion + "|" +  self.__idEmpleado + "\n")

        archivo.close()
    
    def eliminarInfo(self):
        archivo = open("./archivos/Cursos.txt","r",encoding ='utf8')
        guardCurso = []
        for renglon in archivo:
            datos = renglon.split("\n")
            if datos[0] != (self.__idCurso + "|" + self.__descripcion + "|" + self.__idEmpleado):
                guardCurso.append(datos[0])
                archivo2 = open("./archivos/Cursos.txt","w",encoding = "utf8")
                for i in guardCurso:
                    archivo2.write(i + "\n")
                archivo2.close()
        guardCurso.remove()
        archivo.close()
    
    def cambiarInfo(self):
        lista1 = []
        cam = []
        archivo = open("./archivos/Cursos.txt","r",encoding ='utf8')
        guardar = archivo.readlines()
        for gard in guardar:
            gard = gard.replace("\n", "")
            lista1.append(gard)
        for renglon in lista1:
            datos = renglon.split("|")
            if datos[0] == (self.__idCurso):
                datosNuevos = datos[1].replace(datos[1], self.__descripcion + "|" + self.__idEmpleado + "\n")
                datosCambiados = (datos[0] + "|" + datosNuevos)
                cam.append(datosCambiados)
            else:
                datos = (renglon + "\n")
                cam.append(datos)
        archivos2 = open("./archivos/Cursos.txt","w",encoding = "utf8")                
        for c in cam:
            cambios = c
            archivos2.write(cambios)       
        archivos2.close()
        
        archivo.close()


    





    