import os


class Curso_Tema:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.idCursoTema = idCursoTema
        self.idCurso = idCurso
        self.idTema = idTema


    def añadir_curso_tema(self):
        self.archivo = open("./archivos/cursos_temas.txt","a",encoding="utf8")
        
        print("Cual es el id del curso")
        self.idcursotema = input("> ")
        print("Cual es el id del curso")
        self.idcurso = input("> ")
        print("Cual es el id del curso")
        self.idtema = input("> ")

        self.archivo.write(self.idcursotema + "|" + self.idcurso + "|" + self.idtema + "\n")
        
        self.archivo.close()

    def buscar_curso_tema(self):
        self.archivo = open("./archivos/cursos_temas.txt",encoding="utf8")

        print(self.archivo.read())

        self.archivo.close()


    def detalles_curso_tema(self):
        self.archivo = open("./archivos/cursos_temas.txt",encoding="utf8")

        print("Cual es el id que necesitas")
        self.id_buscar = input("> ")


        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_buscar == id:
                    print(renglon)
                    break

        

        self.archivo.close()


    def modificar_cursos_temas(self):
        self.archivo = open("./archivos/cursos_temas.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/cursos_temas_temp.txt","w",encoding="utf8")

        print("Cual es el id que quieres modificar")
        self.id_mod = input("> ")
        print("Cual es el  nuevo id del tema del curso")
        self.idcursotema = input("> ")
        print("Cual es el nuevo id del curso")
        self.idcurso = input("> ")
        print("Cual el nuevo id del tema")
        self.idtema = input("> ")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_mod != id:
                self.archivo_temp.write(renglon)
            elif self.id_mod == id:
                 self.archivo_temp.write(self.idcursotema + "|" + self.idcurso + "|" + self.idtema + "\n")
                   
    
        self.archivo.close()
        self.archivo_temp.close()

        
        archivo.close()
        archivo_temp.close()

        os.remove("./archivos/cursos_temas.txt")
        os.rename("./archivos/cursos_temas_temp.txt","./archivos/cursos_temas.txt")


    def eliminar_curso_tema(self):
        self.archivo = open("./archivos/cursos_temas.txt","r",encoding="utf8")
        self.archivo_temp = open("./archivos/cursos_temas_temp.txt","w",encoding="utf8")


        print("Id a eliminar")
        self.id_borrar = input("> ")

        for renglon in self.archivo:
           id = renglon.split("|")[0]
           if self.id_borrar != id:
                self.archivo_temp.writen(renglon)

    
        self.archivo.close()
        self.archivo_temp.close()
        os.remove("./archivos/cursos_temas.txt")
        os.rename("./archivos/cursos_temas_temp.txt","./archivos/cursos_temas.txt")

        
        I = Curso_Tema(0,0,0)
        I.eliminar_curso_tema()

