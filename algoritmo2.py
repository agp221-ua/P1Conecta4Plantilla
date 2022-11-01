# ALEJANDRO GALAN PEREZ - 24435563H - GRUPO 3
import time

from nodo2 import Nodo2


# busca en col la primera celda vacía
def busca(tablero, col):
    if tablero.getCelda(0, col) != 0:
        i = -1
    i = 0
    while i < tablero.getAlto() and tablero.getCelda(i, col) == 0:
        i = i + 1
    i = i - 1
    return i


# llama al algoritmo que decide la jugada
def juega2(tablero, posicion):
    Nodo2.IA_NUM = 1
    Nodo2.OTHER_NUM = 2
    nodo = Nodo2(tablero, -1, -1, Nodo2.STARTING_LEVEL, True, Nodo2.MIN_VALUE, Nodo2.MAX_VALUE)
    posicion[0] = tablero.queFilaDisp(nodo.colSol)
    posicion[1] = nodo.colSol
    Nodo2.nodos_hasta_el_momento = 0
