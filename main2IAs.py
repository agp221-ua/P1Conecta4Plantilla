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


def main(a):
    # for cuatro in range(a[0], a[1], 500):
    #     for trio in range(100, cuatro, int(cuatro * 0.11)):
    #         for pareja in range(10, trio, int(trio * 0.11)):
    #             global GLOBAL_SAVE
    #             jugando(pareja, trio, cuatro, a[2])
    jugando()


def jugando():
    nueva = 0
    vieja = 0
    empate = 0
    #Nodo.probandoValores(pareja, trio, cuatro)
    for i in range(1, 3):
        #print('--------------------------------------------------------------')
        for ii in range(0, 8):
            #print(".", end="")
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
                        # print("Gana Nodo2" + str(posicion))
                        # print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        # print("Gana Nodo" + str(posicion))
                        # print(str(tablero))
                        break
                    if tablero.empate():
                        empate += 1
                        # print(str(tablero))
                        # break
                    posicion = [-1, -1]
                    juega2(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 1)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        # print("Gana Nodo2" + str(posicion))
                        # print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        # print("Gana Nodo" + str(posicion))
                        # print(str(tablero))
                        break
                else:
                    posicion = [-1, -1]
                    juega2(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 1)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        # print("Gana Nodo2" + str(posicion))
                        # print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        # print("Gana Nodo" + str(posicion))
                        # print(str(tablero))
                        break
                    if tablero.empate():
                        empate += 1
                        # print(str(tablero))
                        break
                    posicion = [-1, -1]
                    juega(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 2)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        # print("Gana Nodo2" + str(posicion))
                        # print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        # print("Gana Nodo" + str(posicion))
                        # print(str(tablero))
                        break
    print(f"{10}, {100}, {1000}\n{nueva}  V {vieja}  E {empate}")


if __name__ == "__main__":
    # proceses = []
    # for i in range(1,10):
    #     proceses.append([i*1000,(i+1)*1000,i-1])
        #s = multiprocessing.Process(target=main2, args=(i*1000,(i)*1000,i-1))
        # proceses.append(s)
    # s = multiprocessing.Process(target=main2, args=(10000, 10001, 9))
    # s.start()
    #pool = multiprocessing.Pool(processes=len(proceses))
    #pool.map(main, proceses)
    main(1)


