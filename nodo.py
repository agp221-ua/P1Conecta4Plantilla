import sys



class Nodo:
    """
        La clase Nodo sirve para almacenar de forma visual los diferentes datos y metodos a usar en todo el arbol

        Genera de forma recursiva todos los hijos hasta los casos base.

        Una vez creado, accediendo a .colSol se tiene la columna a colocar la ficha.
    """
    MAX_VALUE = sys.maxsize
    '''Maximo valor que puede tomar un Nodo'''
    MIN_VALUE = -sys.maxsize - 1
    '''Minimo valor que puede tomar un Nodo'''
    nodos_hasta_el_momento = 0
    '''Numero de nodos creados a partir de este nodo (cabe establecerlo a 0 en algoritmo al acabar con el Nodo)'''
    IA_NUM = 2
    '''Numero que va a tomar la IA como si misma'''
    OTHER_NUM = 1
    '''Numero que va a tomar la IA como el enemigo'''
    STARTING_LEVEL = 9
    '''Nivel de profundidad maxima'''
    PAIR_VALUE = 10
    '''Valor de las parejas'''
    TRIO_VALUE = 100
    '''Valor de los trios'''
    FOUR_VALUE = 1000
    '''Valor de los 4 en raya'''
    ORDER = [3, 4, 2, 5, 1, 6, 0, 7]
    '''Orden en el que va a explorar los hijos'''
    F = [-1, -1, -1,0,0,1,1,1]
    '''Orden en el que va a explorar las filas en evalua() al comprobar los vecinos'''
    C = [-1, 0, 1, -1,1,-1,0,1]
    '''Orden en el que va a explorar las filas en evalua() al comprobar los vecinos'''
    memoryzacion = {}
    def __init__(self, tablero, columna, fila_cuatro, nivel, minmax, alpha, beta):
        '''
        Constructor de la clase Nodo. Este construye recursivamente todos sus nodos hijos para obtener la mejor columna dado un tablero.
        :param tablero: Tablero el cual evaluaremos si es un caso base o al cual añadiremos fichas para obtener sus hijos
        :param columna: Columna en la que hemos metido ficha en este hijo (-1 si es raiz)
        :param fila_cuatro: Fila en la que hemos metido ficha en este hijo (-1 si es raiz)
        :param nivel: Nivel del arbol en el que se encuentra el nodo (0 si es hoja; STARTING_LEVEL si es la raiz)
        :param minmax: True si es un nodo MAX; False si es un nodo MIN
        :param alpha: Valor de ALPHA para emplear poda alfa y beta
        :param beta: Valor de BETA para emplear poda alfa y beta
        '''
        Nodo.nodos_hasta_el_momento += 1
        self.valor = self.MIN_VALUE if minmax else self.MAX_VALUE
        '''(Int) Valor del nodo'''
        self.columna = columna
        '''(Int) Columna en la cual se ha metido ficha (-1 si es raiz)'''
        self.colSol = -1
        '''(Int) Variable en la cual reside la columna que ha elegido la IA (al calcularse todo)'''
        self.beta = beta
        '''(Int) Beta para poda alfa y beta'''
        self.alpha = alpha
        '''(Int) Beta para poda alfa y beta'''
        cer = tablero.cuatroEnRayaFast(fila_cuatro, columna)
        #Aqui comprobamos si hay 4 en raya. Si no hay, se evalua si es caso base o se cr
        if cer == 0:
            if nivel != 0 and not(tablero.empate()):
                self.minimax(minmax, tablero, nivel)
            else:
                self.valor = self.evaluate(tablero)
        elif cer == Nodo.IA_NUM:
            self.valor = Nodo.FOUR_VALUE + nivel  # if minmax else -1000
        else:
            self.valor = -Nodo.FOUR_VALUE - nivel


    def evaluate(self, tablero):
        punt = 0
        a = tablero.toKey()
        if a in Nodo.memoryzacion.keys():
            return Nodo.memoryzacion[a]
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
                    ffff = fila - f
                    cccc = col - c
                    if not(0 <= cccc < 8) or f_antes[cccc] != ffff:
                        if tablero.getCelda(ffff, cccc) == this_cell and (tablero.getCelda(ff + f, cc + c) == 0 or tablero.getCelda(ffff - f, cccc - c) == 0):
                            punt += Nodo.TRIO_VALUE if tablero.getCelda(ffff, cccc) == Nodo.IA_NUM else -Nodo.TRIO_VALUE
                            aux = f - c == 0  # the same as (f == 1 and c == 1) or (f == -1 and c == -1)
                            already_evaluated[0] = already_evaluated[0] or aux
                            already_evaluated[1] = already_evaluated[1] or not aux
                            already_evaluated[2] = already_evaluated[2] or f == 0
                            continue
                        if (tablero.getCelda(ffff, cccc) == 0 and tablero.getCelda(fff, ccc) == 0) or (tablero.getCelda(ffff, cccc) == 0 and tablero.getCelda(ffff - f, cccc - c) == 0) or (tablero.getCelda(fff+f, ccc+c) == 0 and tablero.getCelda(fff, ccc) == 0):
                            punt += Nodo.PAIR_VALUE if tablero.getCelda(ff, cc) == Nodo.IA_NUM else -Nodo.PAIR_VALUE
            f_antes[col] = fila
            Nodo.memoryzacion[a] = punt
        return punt

    def minimax(self, minmax, tablero, nivel):
        for i in Nodo.ORDER:
            if self.beta > self.alpha and tablero.queFilaDisp(i) != -1:
                fila = tablero.insertFicha(i, Nodo.IA_NUM if minmax else Nodo.OTHER_NUM)
                hijo = Nodo(tablero, i, fila, nivel - 1, not minmax, self.alpha, self.beta)
                if minmax:
                    self.alpha = max(hijo.valor, self.alpha)
                else:
                    self.beta = min(hijo.valor, self.beta)
                tablero.removeFicha(i, fila)
                valor_antes = self.valor
                self.valor = max(self.valor, hijo.valor) if minmax else min(self.valor, hijo.valor)
                if nivel == Nodo.STARTING_LEVEL:
                    self.colSol = hijo.columna if valor_antes != self.valor else self.colSol

