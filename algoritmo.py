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
    #print('recibido')
    nodo = Nodo(tablero, -1, -1, Nodo.STARTING_LEVEL, True, Nodo.MIN_VALUE, Nodo.MAX_VALUE)
    #print(f"{nodo.colSol} [{nodo.valor}]")
    #ccc = int(input("Columna?: "))
    #posicion[0] = tablero.queFilaDisp(ccc)
    #posicion[1] = ccc
    posicion[0] = tablero.queFilaDisp(nodo.colSol)
    posicion[1] = nodo.colSol
    #print(Nodo.nodos_hasta_el_momento)
    Nodo.nodos_hasta_el_momento = 0  ##cosas de debuggeo
    tiempou2 = time.time()
    ttt = str(tiempou2 - tiempou).split('.')
    print(f'{ttt[0]},{ttt[1]}')
    # print(str(tablero))
    #print("Acabado nuevo")

