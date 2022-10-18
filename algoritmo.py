from nodo import *
import time
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
    tiempou = time.time()
    nodo = Nodo(tablero, None, -1, -1, 8, True, Nodo.MIN_VALUE, Nodo.MAX_VALUE)
    posicion[0] = tablero.queFilaDisp(nodo.colSol)
    posicion[1] = nodo.colSol
    #Nodo.nodos_hasta_el_momento = 0  ##cosas de debuggeo
    tiempou2 = time.time()
    print(f"Acabao a los {tiempou2 - tiempou} segundos")
    #print("Acabado nuevo")
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

