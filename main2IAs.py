import multiprocessing
import threading

from tablero import *
from algoritmo import *
from algoritmo2 import *

MARGEN = 20
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
TAM = 60
COSA = [-1,-1,1,-1,-1,-1,1,-1]


def main():
    jugando()


def jugando():
    nueva = 0
    vieja = 0
    empate = 0
    for i in range(1, 3):
        for ii in range(0, 8):
            tablero = Tablero(None)
            tablero.setCelda(6, ii, i)
            while True:
                if i == 1:
                    posicion = [-1, -1]
                    juega(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 2)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        print("Gana Nodo2" + str(posicion))
                        print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        print("Gana Nodo" + str(posicion))
                        print(str(tablero))
                        break
                    if tablero.empate():
                        empate += 1
                        print(str(tablero))
                        break
                    posicion = [-1, -1]
                    juega2(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 1)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        print("Gana Nodo2" + str(posicion))
                        print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        print("Gana Nodo" + str(posicion))
                        print(str(tablero))
                        break
                else:
                    posicion = [-1, -1]
                    juega2(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 1)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        print("Gana Nodo2" + str(posicion))
                        print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        print("Gana Nodo" + str(posicion))
                        print(str(tablero))
                        break
                    if tablero.empate():
                        empate += 1
                        print(str(tablero))
                        break
                    posicion = [-1, -1]
                    juega(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 2)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        print("Gana Nodo2" + str(posicion))
                        print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        print("Gana Nodo" + str(posicion))
                        print(str(tablero))
                        break


if __name__ == "__main__":
    main()


