class Alumno:
    def __init__(self):
        self.alumnoNew = ()
        self.respu = ()
        self.a = ()
        self.b = ()
        self.c = ()

    def nuevoAlumno(self):
        alumnoNew = []
        print(" ")
        print("Formulario de ingreso de alumnos")
        print("-----------------------------------")
        respu = input("¿Quiere resgistrar al alumno? (S/F): ")
        while respu == "S" or respu == "s":
            print("Ingrese el nombre y apellidos: ")
            a = input()
            print("Ingrese direccion: ")
            b = input()
            print("Ingrese edad actual: ")
            c = int(input())
            alumnoNew.append((a, b, c))
            respu = input("¿Quiere resgistrar al otro alumno? (S/F): ")
        print(" ")
        print("Datos guardados")
        print("-----------------------------------")
        for x in range(len(alumnoNew)):
            print("[Nombre y apellido: ", alumnoNew[x][0], "] [domicilio: ", alumnoNew[x][1], "] [edad: ",
                  alumnoNew[x][2], "]")
        print(" ")
        print(" ")
        print(" ")
        return None

Alumno().nuevoAlumno()