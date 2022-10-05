class Nodo:
    def __init__(self, tablero, nodo_padre, columna, nivel, minmax):
        self.tablero = tablero
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
                    if (self.tablero.queFilaDisp(i) != -1):
                        fila = self.tablero.insertFicha(i, 2 if minmax else 1)
                        padre = self
                        self.hijos.append(Nodo(self.tablero, padre, i, nivel - 1, not minmax))
                        self.tablero.removeFicha(i, fila)
            self.valor = self.calcular_valor()
            # if not self.minmax:
            #     self.valor *= -1
        elif cer == 2:
            self.valor = 1000# if minmax else -1000
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
        if self.getIANum() == self.tablero.getCelda(fila, col):
            for f in range(-1, 2):
                for c in range(-1, 2):
                    ff = fila + f
                    cc = col + c
                    # Aqui entra si hay pareja
                    if self.tablero.getCelda(ff, cc) == self.valor:
                        fff = ff + f
                        ccc = cc + c
                        # Aqui entra si hay trio tomando como extremo el del [fila,col]
                        if self.tablero.getCelda(fff, ccc) == self.valor:
                            punt += 10
                        else:
                            fff = fila - f
                            ccc = col - c
                            if self.tablero.getCelda(fff, ccc) == self.valor:
                                punt += 10
                            else:
                                punt += 1
        elif self.tablero.getCelda(fila, col) != 0:
            for f in range(-1, 2):
                for c in range(-1, 2):
                    ff = fila + f
                    cc = col + c
                    # Aqui entra si hay pareja
                    if self.tablero.getCelda(ff, cc) == self.valor:
                        fff = ff + f
                        ccc = cc + c
                        # Aqui entra si hay trio tomando como extremo el del [fila,col]
                        if self.tablero.getCelda(fff, ccc) == self.valor:
                            punt -= 10
                        else:
                            fff = fila - f
                            ccc = col - c
                            if self.tablero.getCelda(fff, ccc) == self.valor:
                                punt -= 10
                            else:
                                punt -= 1
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
            mejor = -1 if self.minmax else 300000
            for i in range(0, len(self.hijos)):
                val = self.hijos[i].valor
                mejor = max(mejor, val) if self.minmax else min(mejor, val)
            return mejor

    def __str__(self):
        if self.nivel == 0:
            return 'h:' + str(self.valor)
        else:
            s = "n:" + str(self.valor) + ' | '
            for i in range(0,len(self.hijos)):
                s += str(self.hijos[i].valor) + ' '
            return s