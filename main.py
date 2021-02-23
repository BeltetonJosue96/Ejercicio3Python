import copy
class NuevoSemestre:
    def __init__(self):
        self.op = ()
        self.Alumno = ()
        self.Curso = ()
        self.Ciclo = ()
        self.Seccion = ()


    def menu(self):
        while True:
            print(" ")
            print("- - - - BIENVENIDO A UNIVERSIDAD SOLOPA - - - -")
            print("Instrucciones generales")
            print(" ")
            print("Primero debera registrar: alumnos, cursos, ciclos y secciones")
            print("Segundo debera realizar la asignacion de cursos")
            print(" ")
            print("-----------------------------------------------")
            print("Menu de acceso")
            print("Seleccione una de las siguientes opciones: ")
            print("  1)  Registrar cursos")
            print("  2)  Registrar ciclos")
            print("  3)  Registrar secciones")
            print("  4)  Registrar alumnos")
            print("  5)  Matricular alumnos")
            print("  6)  Visualizar matriculas realizadas")
            print("  7)  Salir del programa")
            op = input("Ingrese el numero de la opcion deseada >>> ")
            if op == "1":
                print(" ")
                input("Has pulsado la opción 1, Registrar cursos...\npulsa una tecla para continuar")
                from curso import Curso
            elif op == "2":
                print(" ")
                input("Has pulsado la opción 2, Registrar ciclos...\npulsa una tecla para continuar")
                from ciclo import Ciclo
            elif op == "3":
                print(" ")
                input("Has pulsado la opción 3, Registrar secciones...\npulsa una tecla para continuar")
                from seccion import Seccion
            elif op == "4":
                print(" ")
                input("Has pulsado la opción 4, Registrar alumnos...\npulsa una tecla para continuar")
                from alumno import Alumno
            elif op == "5":
                print(" ")
                input("Has pulsado la opción 5, Matricular alumnos...\npulsa una tecla para continuar")
                NuevoSemestre().matricular()
            elif op == "6":
                print(" ")
                input("Has pulsado la opción 6, Visualizar matriculas...\npulsa una tecla para continuar")
                NuevoSemestre().visualizar()
            elif op == "7":
                print(" ")
                input("Has pulsado la opción 7, Salir del programa...\npulsa una tecla para continuar")
                print(" ")
                print("Adios.....")
                break
            else:
                print("")
                input("Has pulsado la opción invalida...\npulsa una tecla para volver a intentar")

    def memoriaDinamica(self):
        memoriaSeccion = []
        ms = input()

    def matricular(self):
        pass

    def visualizar(self):
        pass

Semestre = NuevoSemestre()
Semestre.menu()
