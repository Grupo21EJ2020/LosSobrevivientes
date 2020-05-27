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
        return self.__direccion =valor 
           