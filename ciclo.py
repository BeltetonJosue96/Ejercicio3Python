class Ciclo:
    def __init__(self):
        self.cicloNew = ()
        self.respu = ()
        self.a = ()
        self.b = ()
        self.c = ()

    def nuevoCiclo(self):
        cicloNew = []
        print(" ")
        print("Formulario de ingreso de ciclos")
        print("-----------------------------------")
        respu = input("¿Quiere resgistrar un ciclo? (S/F): ")
        while respu == "S" or respu == "s":
            print("Ingrese el numero de semestre (1 o 2): ")
            a = int(input())
            print("Ingrese año: ")
            b = int(input())
            cicloNew.append((a, b))
            respu = input("¿Quiere resgistrar otro ciclo? (S/F): ")
        print(" ")
        print("Datos guardados")
        print("-----------------------------------")
        for x in range(len(cicloNew)):
            print("[Numero de semestre: ", cicloNew[x][0], "] [año: ", cicloNew[x][1],"]")
        print(" ")
        print(" ")
        print(" ")
        return None

Ciclo().nuevoCiclo()