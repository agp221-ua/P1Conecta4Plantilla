# ALEJANDRO GALAN PEREZ - 24435563H - GRUPO 3
from nodo import Nodo
from tablero import Tablero


class Junit:
    ALTO = 7
    ANCHO = 8
    PAIR = 10
    TRIO = 100
    FOUR = 1000
    next_id = 0

    def __init__(self, t, ptc1, ptc2, ultima_fila, ultima_col):

        self.id = Junit.next_id
        Junit.next_id += 1
        self.tablero = Tablero(None)
        for i in range(0, Junit.ALTO):
            for j in range(0, Junit.ANCHO):
                self.tablero.tablero[i][j] = t[i][j]
                if t[i][j] != 0 and self.tablero.disponible[j] >= i:
                    self.tablero.disponible[j] = i - 1
        self.ptc1 = ptc1
        self.ptc2 = ptc2
        self.ultima_fila = ultima_fila
        self.ultima_col = ultima_col

    def __str__(self):
        salida = "  0 1 2 3 4 5 6 7\n"
        for f in range(Junit.ALTO):
            salida += str(f) + " "
            for c in range(Junit.ANCHO):
                if self.tablero.tablero[f][c] == 0:
                    salida += ". "
                elif self.tablero.tablero[f][c] == 1:
                    salida += "1 "
                elif self.tablero.tablero[f][c] == 2:
                    salida += "2 "
            salida += "\n"
        salida += f"Res. 1 {self.ptc1}   2 {self.ptc2}\n"
        return salida

    def JAssert(self):
        res = 0
        res += self.ptc2[0] * Junit.PAIR
        res += self.ptc2[1] * Junit.TRIO
        res += self.ptc2[2] * Junit.FOUR
        res -= self.ptc1[0] * Junit.PAIR
        res -= self.ptc1[1] * Junit.TRIO
        res -= self.ptc1[2] * Junit.FOUR
        val = self.calculandoNodoUser()
        print(f"[Junit {self.id}] Calculado correctamente" if (
                    res == val) else f"[Junit {self.id}] Calculado ERRONEAMENTE: Esperado [{res}] - Obtenido [{val}]")

    def calculandoNodoUser(self):
        Nodo.STARTING_LEVEL = 0
        nodo = Nodo(self.tablero, self.ultima_col, self.ultima_fila, 0, True, Nodo.MIN_VALUE, Nodo.MAX_VALUE)
        return nodo.valor


def main():
    junits = []
    file = open("tableros.txt")
    aux = []
    for l in file:
        if l.startswith('#'):
            continue
        if l.startswith(' '):
            auxx = l.removeprefix(' ').split(' ')
            aa = []
            for x in auxx[0].split('/'):
                aa.append(int(x))
            bb = []
            for x in auxx[1].split('/'):
                bb.append(int(x))

            junits.append(Junit(aux, aa, bb, int(auxx[2]), int(auxx[3])))
            aux = []
        else:
            a = l.removesuffix('\n').split(' ')
            b = []
            for x in a:
                b.append(int(x))
            aux.append(b)

    for x in junits: x.JAssert()


if __name__ == "__main__":
    main()
