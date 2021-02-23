class Seccion:
    def __init__(self):
        self.seccNew = ()
        self.respu = ()
        self.a = ()
        self.b = ()
        self.c = ()

    def nuevaSeccion(self):
        seccNew = []
        print(" ")
        print("Formulario de ingreso de secciones")
        print("-----------------------------------")
        respu = input("¿Quiere resgistrar una seccion? (S/F): ")
        while respu == "S" or respu == "s":
            print(" ")
            print("Datos guardados de secciones existentes")
            print("-----------------------------------")
            for x in range(len(seccNew)):
                print("[Seccion: ", seccNew[x][0],"]")
            print(" ")
            print(" ")
            print(" ")
            print("Ingrese letra de la seccion (favor no repita datos ya guardados): ")
            a = input()
            seccNew.append((a))
            respu = input("¿Quiere resgistrar otra seccion? (S/F): ")

        print(" ")
        return None

Seccion().nuevaSeccion()