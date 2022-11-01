# ALEJANDRO GALAN PEREZ - 24435563H - GRUPO 3
from nodo import *


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
def juega(tablero, posicion):
    nodo = Nodo(tablero, -1, -1, Nodo.STARTING_LEVEL, True, Nodo.MIN_VALUE, Nodo.MAX_VALUE)
    posicion[0] = tablero.queFilaDisp(nodo.colSol)
    posicion[1] = nodo.colSol
    Nodo.nodos_hasta_el_momento = 0  ##cosas de debuggeo
