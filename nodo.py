import sys




class Nodo:
    MAX_VALUE = sys.maxsize
    MIN_VALUE = -sys.maxsize - 1
    nodos_hasta_el_momento = 0
    IA_NUM = 2
    PAIR_VALUE = 18
    TRIO_VALUE = 30
    FOUR_VALUE = 100
    COL_VALUES = [0,1,2,3,3,2,1,0]

    def __init__(self, tablero, nodo_padre, columna, fila_cuatro, nivel, minmax, alpha, beta):
        Nodo.nodos_hasta_el_momento += 1
        self.tablero = tablero
        self.alpha = alpha
        self.beta = beta
        # min false, max true
        self.minmax = minmax
        self.nivel = nivel
        self.valor = -1
        self.nodoPadre = nodo_padre
        self.columna = columna
        self.hijos = []
        #cer = self.tablero.cuatroEnRaya()
        cer = self.tablero.cuatroEnRayaFast(fila_cuatro, columna)
        if cer == 0:
            if nivel != 0:
                for i in range(0, 8):
                    if self.tablero.queFilaDisp(i) != -1:
                        if self.beta <= self.alpha:
                            break
                        fila = self.tablero.insertFicha(i, 2 if minmax else 1)
                        self.hijos.append(Nodo(self.tablero, self, i, fila, nivel - 1, not minmax, self.alpha, self.beta))
                        if minmax:
                            self.alpha = max(self.hijos[-1].valor, self.alpha)
                        else:
                            self.beta = min(self.hijos[-1].valor, self.beta)
                        self.tablero.removeFicha(i, fila)

            self.valor = self.calcular_valor()
        elif cer == Nodo.IA_NUM:
            self.valor = Nodo.FOUR_VALUE + self.nivel  # if minmax else -1000
        else:
            self.valor = -Nodo.FOUR_VALUE - self.nivel
        self.colSol = -1
        if self.nodoPadre is None:
            for i in self.hijos:
                if i.valor == self.valor:
                    self.colSol = i.columna
                    break

    def possible4line(self):
        return True

    def evaluate(self):
        punt = self.COL_VALUES[self.columna] * 1 if self.minmax else -1
        for col in range(0, 8):
            fila = self.tablero.queFilaDisp(col)
            if fila != -1:
                fila = self.tablero.getAlto() - 1 if fila == self.tablero.getAlto() - 1 else fila + 1

                this_cell = self.tablero.getCelda(fila, col)
                if this_cell == 0:
                    continue
                f_antes = [-1, -1, -1, -1, -1, -1, -1, -1]
                already_evaluated = [False, False, False]  # Diagonal izq, Diagonal der, Horizontal
                for f in range(0, 8):
                    for c in range(0, 8):
                        if f == 0 and c == 0:
                            continue
                        ff = fila + f
                        cc = col + c
                        if cc >= 0 and c == -1 and ff == f_antes[cc] :
                            continue
                        if self.tablero.getCelda(ff, cc) == this_cell:
                            fff = ff + f
                            ccc = cc + c
                            if self.tablero.getCelda(fff, ccc) == this_cell and (self.tablero.getCelda(fff+f,ccc+c) or self.tablero.getCelda(fila-f,col-c) == 0):
                                punt += Nodo.TRIO_VALUE if self.tablero.getCelda(fff, ccc) == Nodo.IA_NUM else -Nodo.TRIO_VALUE
                                continue
                            if (already_evaluated[0] and f == 1 and c == 1) or (already_evaluated[1] and f == 1 and c == -1) or (already_evaluated[2] and f == 0 and c == 1):
                                continue
                            fff = fila - f
                            ccc = col - f
                            if self.tablero.getCelda(fff, ccc) == this_cell and (self.tablero.getCelda(ff+f,cc+c) or self.tablero.getCelda(fff-f,ccc-c) == 0):
                                punt += Nodo.TRIO_VALUE if self.tablero.getCelda(fff, ccc) == Nodo.IA_NUM else -Nodo.TRIO_VALUE
                                aux = f - c == 0 # the same as (f == 1 and c == 1) or (f == -1 and c == -1)
                                already_evaluated[0] = already_evaluated[0] or aux
                                already_evaluated[1] = already_evaluated[1] or not aux
                                already_evaluated[2] = already_evaluated[2] or f == 0
                                continue
                            punt += Nodo.PAIR_VALUE if self.tablero.getCelda(ff, cc) == Nodo.IA_NUM else -Nodo.PAIR_VALUE
        return punt

    def calcular_valor(self):
        if self.nivel == 0:
            return self.evaluate()
        else:
            mejor = self.MIN_VALUE if self.minmax else self.MAX_VALUE
            for i in range(0, len(self.hijos)):
                val = self.hijos[i].valor
                mejor = max(mejor, val) if self.minmax else min(mejor, val)
            return mejor

    def __str__(self):
        # Este metodo se ha creado unicamente para debuguear, no se usa en el algoritmo
        if self.nivel == 0:
            return 'h:' + str(self.valor)
        else:
            s = "n:" + str(self.valor) + ' | '
            for i in range(0, len(self.hijos)):
                s += str(self.hijos[i].valor) + ' '
            return s

    @staticmethod
    def probandoValores(pareja, trio, cuatro):
        Nodo.PAIR_VALUE = pareja
        Nodo.TRIO_VALUE = trio
        Nodo.FOUR_VALUE = cuatro