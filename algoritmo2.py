import time

from nodo import *
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
    t1 = time.time()
    nodo = Nodo2(tablero, -1, -1, Nodo2.STARTING_LEVEL, True, Nodo.MIN_VALUE, Nodo.MAX_VALUE)
    t2 = time.time()
    #print(t2 - t1)
    posicion[0] = tablero.queFilaDisp(nodo.colSol)
    posicion[1] = nodo.colSol
    #print("Acabao viejo")

    ####################################################
    ## sustituir este código por la llamada al algoritmo
    #
    # enc = False
    # c = 0
    # while not enc and c < tablero.getAncho():
    #     f = busca(tablero, c)
    #     if f != -1:
    #         enc = True
    #     else:
    #         c = c + 1
    # if f != -1:
    #     posicion[0] = f
    #     posicion[1] = c
    ####################################################

