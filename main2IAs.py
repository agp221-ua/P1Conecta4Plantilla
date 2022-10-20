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


def main():
    # for cuatro in range(1000, 10001, 500):
    #     for trio in range(100, cuatro, int(cuatro * 0.05)):
    #         for pareja in range(10, trio, int(trio * 0.1)):
    #             print(f"PROBANDO CON VALORES {pareja}, {trio}, {cuatro}")
    #             res = jugando(pareja, trio, cuatro)
    jugando(10, 100, 1000)


def jugando(pareja, trio, cuatro):
    nueva = 0
    vieja = 0
    empate = 0
    #Nodo.probandoValores(pareja, trio, cuatro)
    for i in range(1, 3):
    #for i in range(2, 3):
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        for ii in range(0, 8):
        #for ii in range(7,8):
            #print(".", end="")
            tablero = Tablero(None)
            tablero.setCelda(6, ii, i)
            while True:
                posicion = [-1, -1]
                if i == 1:
                    posicion = [-1, -1]
                    juega(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 2)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        print("Gana Nodo2")
                        print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        print("Gana Nodo")
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
                        print("Gana Nodo2")
                        print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        print("Gana Nodo")
                        print(str(tablero))
                        break
                else:
                    posicion = [-1, -1]
                    juega2(tablero, posicion)
                    tablero.setCelda(posicion[0], posicion[1], 1)
                    res = tablero.cuatroEnRaya()
                    if res == 1:
                        vieja += 1
                        print("Gana Nodo2")
                        print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        print("Gana Nodo")
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
                        print("Gana Nodo2")
                        print(str(tablero))
                        break
                    if res == 2:
                        nueva += 1
                        print("Gana Nodo")
                        print(str(tablero))
                        break
    print(f"\n------------------------------------------------------ RESULTADO: N {nueva}  V {vieja}  E {empate}")
    return [nueva, vieja, empate]




if __name__ == "__main__":
    main()
