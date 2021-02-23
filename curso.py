class Curso:
    def __init__(self):
        self.cursoNew = ()
        self.respu = ()
        self.a = ()
        self.b = ()
        self.c = ()

    def nuevoCurso(self):
        cursoNew = []
        print(" ")
        print("Formulario de ingreso de cursos")
        print("-----------------------------------")
        respu = input("¿Quiere resgistrar un curso? (S/F): ")
        while respu == "S" or respu == "s":
            print("Ingrese el nombre del curso: ")
            a = input()
            print("Ingrese codigo de referencia: ")
            b = int(input())
            cursoNew.append((a, b))
            respu = input("¿Quiere resgistrar otro curso? (S/F): ")
        print(" ")
        print("Datos guardados")
        print("-----------------------------------")
        for x in range(len(cursoNew)):
            print("[Nombre del curso: ", cursoNew[x][0], "] [codigo de curso: ", cursoNew[x][1],"]")
        print(" ")
        print(" ")
        print(" ")
        return None

Curso().nuevoCurso()