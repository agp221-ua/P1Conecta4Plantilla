import sys


class Nodo:
    MAX_VALUE = sys.maxsize
    MIN_VALUE = -sys.maxsize - 1

    def __init__(self, tablero, nodo_padre, columna, nivel, minmax, alpha, beta):
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
        cer = self.tablero.cuatroEnRaya()
        if cer == 0:
            if (nivel != 0):
                for i in range(0, 8):
                    if self.tablero.queFilaDisp(i) != -1:
                        if self.beta <= self.alpha:
                            break
                        fila = self.tablero.insertFicha(i, 2 if minmax else 1)
                        self.hijos.append(Nodo(self.tablero, self, i, nivel - 1, not minmax, alpha, beta))
                        if minmax:
                            self.alpha = self.hijos[-1].valor
                        else:
                            self.beta = self.hijos[-1].valor
                        self.tablero.removeFicha(i, fila)

            self.valor = self.calcular_valor()
        elif cer == 2:
            self.valor = 1000  # if minmax else -1000
        else:
            self.valor = -1000
        self.colSol = -1
        if self.nodoPadre is None:
            for i in self.hijos:
                if i.valor == self.valor:
                    self.colSol = i.columna
                    break

    def getIANum(self):
        return 2

    def calcular_parejas_trios(self, fila, col):
        punt = 0
        thisCelda = self.tablero.getCelda(fila, col)
        if 0 != thisCelda:
            for f in range(-1, 2):
                for c in range(-1, 2):
                    ff = fila + f
                    cc = col + c
                    # Aqui entra si hay pareja
                    if self.tablero.getCelda(ff, cc) == thisCelda:
                        fff = ff + f
                        ccc = cc + c
                        # Aqui entra si hay trio tomando como extremo el del [fila,col]
                        if self.tablero.getCelda(fff, ccc) == thisCelda:
                            ffff = fff + f
                            cccc = ccc + c
                            aux = self.tablero.getCelda(ffff, cccc)
                            fffff = fila - f
                            ccccc = col - c
                            aux2 = self.tablero.getCelda(fffff, ccccc)
                            # Aqui entra si se pudiera en un futuro hacer 4raya con ese trio, porque si no es inutil
                            if aux == 0 or (aux != 0 and aux2 == 0):
                                punt += 10 if self.tablero.getCelda(fila, col) == self.getIANum() else -10
                        # Aqui entra a ver si resulta que hay trio siendo this el central
                        else:
                            fff = fila - f
                            ccc = col - c
                            # Aqui entra si el opuesto a (ff,cc) respecto a thisCelda es haciendo 3 en raya
                            # Podria mirar a ver en un momento dado si es expandible, pero no merece la pena
                            if self.tablero.getCelda(fff, ccc) == thisCelda:
                                punt += 10 if self.tablero.getCelda(fila, col) == self.getIANum() else -10
                            else:
                                punt += 5 if self.tablero.getCelda(fila, col) == self.getIANum() else -5

        return punt

    def calcular_valor_hoja(self):
        punt = self.columna if (self.columna <= 3) else (self.tablero.getAncho() - self.columna - 1)
        punt = punt if self.minmax else punt * -1
        for i in range(0, 8):
            fila = self.tablero.queFilaDisp(i)
            if fila == -1:
                continue
            fila = 6 if (fila == 6) else fila + 1
            punt += self.calcular_parejas_trios(fila, i)
        return punt

    def calcular_valor(self):
        if self.nivel == 0:
            return self.calcular_valor_hoja()
        else:
            mejor = self.MIN_VALUE if self.minmax else self.MAX_VALUE
            for i in range(0, len(self.hijos)):
                val = self.hijos[i].valor
                mejor = max(mejor, val) if self.minmax else min(mejor, val)
            return mejor

    def __str__(self):
        if self.nivel == 0:
            return 'h:' + str(self.valor)
        else:
            s = "n:" + str(self.valor) + ' | '
            for i in range(0, len(self.hijos)):
                s += str(self.hijos[i].valor) + ' '
            return s
