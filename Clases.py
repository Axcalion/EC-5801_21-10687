

class Matriz:
    # Se ejecuta cada vez que creamos una nueva matriz
    def __init__(self, nombreMatriz, M , N):
        
        # caracteristicas basicas de una matriz
        self.nombre: str = nombreMatriz
        self.filas: int = M
        self.columnas: int = N
        
        # estructura de la matriz
        self.matriz = [None] * self.filas
        
        # llenamos la matriz con filas de ceros antes de inicializarla 
        for i in range(self.filas):
            filaActual: list[int] = [0] * self.columnas
            self.matriz[i] = filaActual
    
    # Metodo para IMPRIMIR la matriz de forma ordena en la consola
    def imprimir(self):
        print(f"Matriz {self.nombre} de tamano {self.filas}x{self.columnas}")
        
        # imprime cada fila de la matriz, una debajo de la otra
        for i in self.matriz:
            print(i)
    
    # Metodo para MODIFICAR un solo numero en una posicion especifica (M , N)         
    def insertar(self, M: int, N: int, dato: int) -> None:
        
        #  el condicional verifica que la coordenada existe dentro del tamano estalecido 
        if 0 <= M < self.filas and 0 <= N < self.columnas:
            self.matriz[M][N] = dato
        else:
            pass
    
    # Metodo para MODIFICAR una fila completa
    def insertarFila(self , numFila: int, nuevaFila: list[int]):
        
        # verifica que la fila nueva sea del tamano correcto
        if len(nuevaFila) != self.columnas:
            print("la fila no es del tamano correcto")        
        else:
            pass
        
        # verifica que el numero de fila que queremos reemplazar si exita
        if 0 <= numFila < self.filas:
            self.matriz[numFila] = nuevaFila
        else:
            pass
        
    # METODOS DE OPERACIONES MATEMATICAS
    # Metodo para SUMAR dos matrices entre si 
    def __add__(self , other: 'Matriz'):
        
        # solo se suman si son exactamente del mismo tamaño
        if self.filas != other.filas or self.columnas != other.columnas:
            print("la matriz no es del tamano correcto")
            return None  
        else:
            pass
        
        # matriz vacia para guardar el resultado
        resultado: 'Matriz' = Matriz("resultado" , self.filas , self.columnas)
        
        # recorre cada casilla sumado los numeros con los de la otra matriz en esa posicion
        for i in range(self.filas):
            for j in range(self.columnas):
                sumPosicion: int = self.matriz[i][j] + other.matriz[i][j]
                
                resultado.matriz[i][j] = sumPosicion
        return resultado
    
    # Metodo para RESTAR dos matrices entre si 
    def __sub__(self , other: 'Matriz'):
        #solo se restan si son exactamente del mismo tamaño
        if self.filas != other.filas or self.columnas != other.columnas:
            print("la matriz no es del tamano correcto")  
            return None
        else:
            pass
        
        # matriz vacia para guardar el resultado
        resultado: 'Matriz' = Matriz("resultado" , self.filas , self.columnas)
        # Recorremos cada casilla restando
        for i in range(self.filas):
            for j in range(self.columnas):
                difPosicion: int = self.matriz[i][j] - other.matriz[i][j]
                
                resultado.matriz[i][j] = difPosicion
        return resultado
    
    # Metodo para MULTIPLICAR dos matrices entre si 
    def __mul__(self, other: 'Matriz'):
        # el numero de columnas de la primera matriz debe ser igual al numero de filas de la otra
        if self.columnas != other.filas:
            print("la matriz no es del tamano correcto")  
            return None
        else:
            pass
        # el resultado se crea tomando las filas de la primera matriz y las columnas de la otra
        resultado = Matriz("resultado" , self.filas , other.columnas)
        
        # filas por Columnas 
        for i in range(self.filas):
            for j in range(other.columnas):
                for k in range(self.columnas):
                    resultado.matriz[i][j] += self.matriz[i][k] * other.matriz[k][j]
                
        return resultado
    
    # intercepta la división, se activa al usar el símbolo (/) 
    def __truediv__(self, other: 'Matriz'):
        
        # bloquea la operacion mostrando el mensaje
        print("la division entre matrices no esta definida")
        return None
                
if __name__ == "__main__":

    #creamos las matrices vacias
    matrizA = Matriz("A" , 3 , 3)
    matrizB = Matriz("B" , 3 , 3)
    matrizC = Matriz("C", 2, 3)
    matrizD = Matriz("D", 3, 2)
    
    # llenamos la matriz A con datos reales
    fila1A: list[int] = [1, 2, 0]
    fila2A: list[int] = [0, 1, 2]
    fila3A: list[int] = [2, 3, 1]
    matrizA.insertarFila(0, fila1A)
    matrizA.insertarFila(1, fila2A)
    matrizA.insertarFila(2, fila3A)
    
    # Llenamos la Matriz B
    fila1B: list[int] = [1, 2, 0]
    fila2B: list[int] = [0, 1, 2]
    fila3B: list[int] = [2, 3, 1]
    matrizB.insertarFila(0, fila1B)
    matrizB.insertarFila(1, fila2B)
    matrizB.insertarFila(2, fila3B)
    
    # Llenamos la Matriz C
    fila1C: list[int] = [1, 2, 0]
    fila2C: list[int] = [0, 1, 2]
    matrizC.insertarFila(0, fila1C)
    matrizC.insertarFila(1, fila2C)
    
    # Llenamos la Matriz D
    fila1D: list[int] = [1, 2]
    fila2D: list[int] = [0, 1]
    fila3D: list[int] = [2, 3]
    matrizD.insertarFila(0, fila1D)
    matrizD.insertarFila(1, fila2D)
    matrizD.insertarFila(2, fila3D)
    
    # Realizamos las operaciones matemáticas
    suma = matrizA + matrizB
    resta = matrizA - matrizB
    multi = matrizC * matrizD
    division: None = matrizA / matrizB
    
    # Imprimimos todas las matrices y los resultados de las operaciones
    matrizA.imprimir()
    matrizB.imprimir()
    matrizC.imprimir()
    matrizD.imprimir()
    suma.imprimir()
    resta.imprimir()
    multi.imprimir()    