import os

class Curso_Tema:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.idCursoTema = idCursoTema
        self.idCurso = idCurso
        self.idTema = idTema
    
    def agregar_curso_tema():
        archivo = open("./archivos/cursos_temas.txt","a",encoding="utf8")
        
        print("Cual es el id del curso")
        idcursotema = input("> ")
        print("Cual es el id del curso")
        idcurso = input("> ")
        print("Cual es el id del curso")
        idtema = input("> ")

        archivo.write(idcursotema + "|" + idcurso + "|" + idtema)
        
        archivo.close()

    def consultar_curso_tema():

        print(archivo.read())

        archivo.close()

    def detalles_curso_tema():
        archivo = open("./archivos/cursos_temas.txt",encoding="utf8")

        print("Cual es el id que necesitas")
        id_buscar = input("> ")

        for renglon in archivo:
            for x in renglon:
                if id_buscar != x:
                    break
                else:
                    print(renglon)
                    break

        archivo.close()

    def modificar_cursos_temas():
        archivo = open("./archivos/cursos_temas.txt","r",encoding="utf8")
        archivo_temp = open("./archivos/cursos_temas_temp.txt","w",encoding="utf8")

        print("Cual es el id que quieres modificar")
        id_mod = input("> ")
        print("Cual es el  nuevo id del tema del curso")
        idcursotema = input("> ")
        print("Cual es el nuevo id del curso")
        idcurso = input("> ")
        print("Cual el nuevo id del tema")
        idtema = input("> ")

        for renglon in archivo:
            for x in renglon:
                if id_mod != x:
                    archivo_temp.write(renglon)
                    break
                elif id_mod == x:
                    archivo_temp.write(idcursotema + "|" + idcurso + "|" + idtema + "\n")
                    break
    
        archivo.close()
        archivo_temp.close()
        os.remove("./archivos/cursos_temas.txt")
        os.rename("./archivos/cursos_temas_temp.txt","./archivos/cursos_temas.txt")

    def borrar_curso_tema():
        archivo = open("./archivos/cursos_temas.txt","r",encoding="utf8")
        archivo_temp = open("./archivos/cursos_temas_temp.txt","w",encoding="utf8")

        print("Id a Borrar")
        id_borrar = input("> ")

        for renglon in archivo:
            for x in renglon:
                if id_borrar != x:
                    archivo_temp.write(renglon)
                    break
                elif id_borrar == x:
                    break
    
        archivo.close()
        archivo_temp.close()
        os.remove("./archivos/cursos_temas.txt")
        os.rename("./archivos/cursos_temas_temp.txt","./archivos/cursos_temas.txt")