class Empleado:
    def __init__(self, idEmpleado,nombre, direccion):
        self.__idEmpleado = idEmpleado
        self.__nombre = nombre
        self.__direccion = direccion

    @property
    def idEmpleado (self):
        return self.__idEmpleado

    @idEmpleado.setter
    def idEmpleado (self,valor):
        self.__idEmpleado = valor 


    @property
    def nombre (self):
        return self.__nombre

    @nombre.setter
    def nombre (self,valor):
        self.__nombre = valor


    @property
    def direccion (self):
        return self.__direccion  

    @direccion.setter
    def direccion (self, valor):
        self.__direccion = valor   

  

    def agregarInfo(self):
        archivo = open("./archivos/Empleados.txt","a",encoding='utf8')

        archivo.write(self.__idEmpleado + "|" + self.__nombre + "|"  + self.__direccion + "\n")

        archivo.close()

    def borrarInfo (self):
        archivo = open("./archivos/Empleados.txt","r",encoding ='utf8')
        lista = []
        for x in archivo:
            datos = x.split("\n")
            if datos[0] != (self.__idEmpleado + "|" + self.__nombre + "|" + self.__direccion):
                lista.append(datos[0])
                archivo2 = open("./archivos/Empleados.txt","w",encoding = "utf8")
                for i in lista:
                    archivo2.write(i + "\n")
                archivo2.close()
        archivo.close()

    

    def modificarInfo (self):
        archivo = open("./archivos/Empleados.txt","a",encoding='utf8')
        cam1 = []
        cam = []
        guardar = archivo.readlines()
        for gard in guardar:
            gard = gard.replace("\n", "")
            cam1.append(gard)
        for renglon in cam1:
            datos = renglon.split("|")
            if datos[0] == (self.__idEmpleado,):
                datosNuevos = datos[1].replace(datos[1], self.__nombre + "|" + self.__direccion + "\n")
                datosCambiados = (datos[0] + "|" + datosNuevos)
                cam.append(datosCambiados)
            else:
                datos = (renglon + "\n")
                cam.append(datos)
        archivos2 = open("./archivos/Empleados.txt","w",encoding = "utf8")                
        for c in cam:
            cambios = c
            archivos2.write(cambios)       
        archivos2.close()
        archivo.close()




             
