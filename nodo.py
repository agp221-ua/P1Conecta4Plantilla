import sys



class Nodo:
    MAX_VALUE = sys.maxsize
    MIN_VALUE = -sys.maxsize - 1
    nodos_hasta_el_momento = 0
    IA_NUM = 2
    OTHER_NUM = 1
    STARTING_LEVEL = 6
    PAIR_VALUE = 10
    TRIO_VALUE = 100
    FOUR_VALUE = 1000
    ORDER = [3, 4, 2, 5, 1, 6, 0, 7]
    F = [-1, -1, -1,0,0,1,1,1]
    C = [-1, 0, 1, -1,1,-1,0,1]

    def __init__(self, tablero, columna, fila_cuatro, nivel, minmax, alpha, beta):  # min false, max true
        Nodo.nodos_hasta_el_momento += 1
        self.valor = -1
        self.hijos = []
        self.columna = columna
        self.colSol = -1
        self.beta = beta
        self.alpha = alpha
        cer = tablero.cuatroEnRayaFast(fila_cuatro, columna)
        if cer == 0:
            if nivel != 0:
                self.minimax(minmax, tablero, nivel)
            else:
                self.valor = self.evaluate(tablero)
        elif cer == Nodo.IA_NUM:
            self.valor = Nodo.FOUR_VALUE + nivel  # if minmax else -1000
        else:
            self.valor = -Nodo.FOUR_VALUE - nivel
        if nivel == Nodo.STARTING_LEVEL:
            for i in self.hijos:
                if i.valor == self.valor:
                    self.colSol = i.columna
                    break

    def evaluate(self, tablero):
        punt = 0
        f_antes = [-1, -1, -1, -1, -1, -1, -1, -1]
        for col in range(0, tablero.getAncho()):
            fila = tablero.queFilaDisp(col)
            fila = tablero.getAlto() - 1 if fila == tablero.getAlto() - 1 else fila + 1
            this_cell = tablero.getCelda(fila, col)
            if this_cell == 0:
                continue
            already_evaluated = [False, False, False]  # Diagonal izq, Diagonal der, Horizontal
            for i in range(0, 8):
                f = Nodo.F[i]
                c = Nodo.C[i]
                ff = fila + f
                cc = col + c
                if c == -1 and cc >= 0 and ff == f_antes[cc]:
                    continue
                if tablero.getCelda(ff, cc) == this_cell:
                    fff = ff + f
                    ccc = cc + c
                    if tablero.getCelda(fff, ccc) == this_cell and f_antes[ccc] != fff and (tablero.getCelda(fff + f, ccc + c) == 0 or tablero.getCelda(fila - f, col - c) == 0):
                        punt += Nodo.TRIO_VALUE if tablero.getCelda(fff, ccc) == Nodo.IA_NUM else -Nodo.TRIO_VALUE
                        continue
                    if (already_evaluated[0] and f == 1 and c == 1) or (already_evaluated[1] and f == 1 and c == -1) or (already_evaluated[2] and f == 0 and c == 1):
                        continue
                    fff = fila - f
                    ccc = col - c
                    if not(0 <= ccc < 8) or f_antes[ccc] != fff:
                        if tablero.getCelda(fff, ccc) == this_cell and (tablero.getCelda(ff + f, cc + c) == 0 or tablero.getCelda(fff - f, ccc - c) == 0):
                            punt += Nodo.TRIO_VALUE if tablero.getCelda(fff, ccc) == Nodo.IA_NUM else -Nodo.TRIO_VALUE
                            aux = f - c == 0  # the same as (f == 1 and c == 1) or (f == -1 and c == -1)
                            already_evaluated[0] = already_evaluated[0] or aux
                            already_evaluated[1] = already_evaluated[1] or not aux
                            already_evaluated[2] = already_evaluated[2] or f == 0
                            continue
                        if tablero.getCelda(ff + f, cc + c) == 0 or tablero.getCelda(fff, ccc) == 0:
                            punt += Nodo.PAIR_VALUE if tablero.getCelda(ff, cc) == Nodo.IA_NUM else -Nodo.PAIR_VALUE
            f_antes[col] = fila
        return punt

    def minimax(self, minmax, tablero, nivel):
        for i in Nodo.ORDER:
            if self.beta > self.alpha and tablero.queFilaDisp(i) != -1:
                fila = tablero.insertFicha(i, Nodo.IA_NUM if minmax else Nodo.OTHER_NUM)
                self.hijos.append(Nodo(tablero, i, fila, nivel - 1, not minmax, self.alpha, self.beta))
                if minmax:
                    self.alpha = max(self.hijos[-1].valor, self.alpha)
                else:
                    self.beta = min(self.hijos[-1].valor, self.beta)
                tablero.removeFicha(i, fila)
        self.valor = self.MIN_VALUE if minmax else self.MAX_VALUE
        for i in self.hijos:
            self.valor = max(self.valor, i.valor) if minmax else min(self.valor, i.valor)

    @staticmethod
    def probandoValores(pareja, trio, cuatro):
        Nodo.PAIR_VALUE = pareja
        Nodo.TRIO_VALUE = trio
        Nodo.FOUR_VALUE = cuatro
