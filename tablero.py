class Tablero:    
    def __init__(self, tabPadre):
        self.ancho=8
        self.alto=7        
        self.tablero=[]
        if tabPadre==None:
            for i in range(self.alto):           
                self.tablero.append([])
                for j in range(self.ancho):
                    self.tablero[i].append(0)
        else:
            for i in range(self.alto):           
                self.tablero.append([])
                for j in range(self.ancho):
                    self.tablero[i].append(tabPadre.getCelda(i,j))          
        
    def __str__(self):
        salida="  0 1 2 3 4 5 6 7\n"
        for f in range(self.alto):
            salida+=str(f)+" "
            for c in range(self.ancho):         
                if self.tablero[f][c] == 0:
                    salida += ". "
                elif self.tablero[f][c] == 1:
                    salida +="1 "
                elif self.tablero[f][c] == 2:
                    salida += "2 "
            salida += "\n"
        return salida
        
                
    def getAncho(self):
        return self.ancho
    
    def getAlto(self):
        return self.alto
    
    def getCelda(self, fila, col):
        if 0 <= fila < self.alto and 0 <= col < self.ancho:
            return self.tablero[fila][col]
        else:
            return -1
    
    def setCelda(self, fila, col, val):
        self.tablero[fila][col]=val

    def queFilaDisp(self, col):
        for i in range(6,-1,-1):
            if(self.getCelda(i,col) == 0):
                return i
        return -1

    def insertFicha(self, col, val):
        fila = self.queFilaDisp(col)
        if(fila != -1):
            self.setCelda(fila,col,val)
        return fila
    def removeFicha(self,col,fila):
        if fila != -1:
            self.setCelda(fila,col, 0)

    def empate(self):
        return self.tablero[0].count(0) == 0

    # detecta si hay cuatro fichas en línea y devuelve el ganador
    def cuatroEnRaya(self):
        i=0        
        fin=False
        ganador=0
        
        while not fin and i<self.getAlto():
            j=0
            while not fin and j<self.getAncho():
                casilla=self.getCelda(i,j)
                if casilla!=0:
                    #búsqueda en horizontal
                    if (j+3) <self.getAncho():
                        if self.getCelda(i, j+1)==casilla and self.getCelda(i, j+2)==casilla and self.getCelda(i, j+3)==casilla:
                            ganador=casilla
                            fin=True
                    #búsqueda en vertical
                    if (i+3) <self.getAlto():
                        if self.getCelda(i+1, j)==casilla and self.getCelda(i+2, j)==casilla and self.getCelda(i+3, j)==casilla:
                            ganador=casilla
                            fin=True
                    #búsqueda en diagonal
                    if (i+3) <self.getAlto():
                        if (j-3) >= 0:
                            if self.getCelda(i+1, j-1)==casilla and self.getCelda(i+2, j-2)==casilla and self.getCelda(i+3, j-3)==casilla:
                                ganador=casilla
                                fin=True
                        if (j+3) <self.getAncho():
                            if self.getCelda(i+1, j+1)==casilla and self.getCelda(i+2, j+2)==casilla and self.getCelda(i+3, j+3)==casilla:
                                ganador=casilla
                                fin=True
                j=j+1
            i=i+1
        return ganador

    def cuatroEnRayaFast(self, fila, col):
        this_cell = self.tablero[fila][col]
        for f in range(-1, 2):
            for c in range(-1, 2):
                if not (f == 0 and c == 0):
                    ff = fila + f
                    cc = col + c
                    if 0 <= ff < self.alto and 0 <= cc < self.ancho and self.tablero[ff][cc] == this_cell:
                        fff = ff + f
                        ccc = cc + c
                        if 0 <= fff < self.alto and 0 <= ccc < self.ancho and self.tablero[fff][ccc] == this_cell:
                            ffff = fff + f
                            cccc = ccc + c
                            if (0 <= ffff < self.alto and
                                0 <= cccc < self.ancho and
                                self.tablero[ffff][cccc] == this_cell) or\
                                    (0 <= fila - f < self.alto and
                                     0 <= col - c < self.ancho and
                                     self.tablero[fila - f][col - c] == this_cell):
                                return this_cell
        return 0
