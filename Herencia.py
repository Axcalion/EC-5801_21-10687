class PuntoPadre:
    
    __x:int
    __y:int
    __z:int
    
    def __init__(self, nombrePunto:str , x:int , y:int , z:int ):
        
        # caracteristicas basicas de un punto
        self.nombre:str = nombrePunto
        self.__x:int = x
        self.__y:int = y
        self.__z:int = z

    # Getters 
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z
    
    # Metodo para IMPRIMIR el punto en la consola        
    def imprimir(self):
        print(f"\n Punto {self.nombre}({self.__x} , {self.__y} , {self.__z})")
    
    # Metodo para SUMAR punto + punto/int  
    def __add__(self, other: 'PuntoPadre' | int):
        
        # si other es un Punto, realizara la operacion de una forma  
        try:
            # obtenemos las nuevas coordenadas
            resultadoX:int = self.__x + other.__x
            resultadoY:int = self.__y + other.__y
            resultadoZ:int = self.__z + other.__z
            
            # al sumar dos puntos obtenemos un tercer punto como resultado
            resultado: PuntoPadre = PuntoPadre("suma" , resultadoX , resultadoY , resultadoZ)
            return resultado
        
        # si other no tiene coords y es solo un numero se sumara a ambas coordenadas 
        except(AttributeError, TypeError):
            # obtenemos las nuevas coordenadas
            resultadoX:int = self.__x + other
            resultadoY:int = self.__y + other
            resultadoZ:int = self.__z + other
            
            # al sumar un escalar obtenemos un segundo punto como resultado
            resultado: PuntoPadre = PuntoPadre(f"{self.nombre} desplazado" , resultadoX , resultadoY , resultadoZ)
            return resultado    
    
    # Metodo para RESTAR punto - punto/int  
    def __sub__(self, other: 'PuntoPadre' | int):
        
        # si other es un Punto, realizara la operacion de una forma  
        try:
            # obtenemos las nuevas coordenadas
            resultadoX:int = self.__x - other.__x
            resultadoY:int = self.__y - other.__y
            resultadoZ:int = self.__z - other.__z
            
            # al restar dos puntos obtenemos un tercer punto como resultado
            resultado: PuntoPadre = PuntoPadre("resta" , resultadoX , resultadoY , resultadoZ)
            return resultado   

        # si other no tiene coords y es solo un numero se sumara a ambas coordenadas
        except(AttributeError, TypeError):
            # obtenemos las nuevas coordenadas
            resultadoX:int = self.__x - other
            resultadoY:int = self.__y - other
            resultadoZ:int = self.__z - other
            
            # al restar un escalar obtenemos un segundo punto como resultado
            resultado: PuntoPadre = PuntoPadre(f"{self.nombre} desplazado" , resultadoX , resultadoY , resultadoZ)
            return resultado  
    # Metodo para MULTIPLICAR por un escalar 
    def __mul__(self , escalar:int):
        
        # obtenemos las nuevas coordenadas
        resultadoX:int = self.__x * escalar
        resultadoY:int = self.__y * escalar
        resultadoZ:int = self.__z * escalar
            
        # al multiplicar un escalar obtenemos obtenemos un nuevo punto
        resultado: PuntoPadre = PuntoPadre(f"{self.nombre}_escalado" , resultadoX , resultadoY , resultadoZ)
        return resultado
    
    # metodo para MULTIPLICAR un escalar por un eje
    def mulEjes(self ,kx: int = 1, ky: int = 1, kz: int = 1 ):
        # multiplicamos eje por eje y obtenemos las nuevas coordenadas
        # al establecre los kn = 1 (n = x , y , z) como base, si solo queremos modficar un eje
        # los demas no se ven afectados
        resultadoX:int = self.__x * kx
        resultadoY:int = self.__y * ky
        resultadoZ:int = self.__z * kz
            
        # al modificar uno o varios ejes obtenemos un nuevo punto  
        resultado: PuntoPadre = PuntoPadre(f"{self.nombre}_modoficado" , resultadoX , resultadoY , resultadoZ)
        return resultado     
        
# representa un vector con origen en (0,0,0)
# hereda estructura y operaciones de la clase PuntoPadre     
class VectorHijo(PuntoPadre):
    
    # Metodo publico para calcular la magnitud del vector
    def magnitud(self):
        """magnitud = raiz caudrada de (x^2 + y^2 + z^2)
         obtenemos el valor de la suma de los cuadrados"""
        sumCuad:int = self.get_x()**2 + self.get_y()**2 + self.get_z()**2

        # aplicamos raiz cuadrada para obtener la magnitud
        magnitud:float = sumCuad**0.5
        return magnitud
    
    
if __name__ == "__main__":

    # creamos dos puntos de prueba
    # diferencia de las matrices, aca podemos llenar todas
    # sus caracteristicas al momento de su creacion
    p1 = PuntoPadre("A", 1, 2, 3)
    p2 = PuntoPadre("B", 1, 2, 3)
    pc = PuntoPadre("C", 1, 1, 1)
    # Suma de puntos
    p3a = p1 + p2

    # Suma de escalar
    p3b = p1 + 1
    
    # resta de puntos
    p4a = p1 - p2 
    
    # resta de escalar
    p4b = p1 - 1
    
    # Multiplicación escalar
    p5 = p1 * 10 

    # Modificacion de un eje
    p6a = pc.mulEjes(kx=5)
    p6b = pc.mulEjes(ky=5)
    p6c = pc.mulEjes(kz=5)
    
    # Modificacion de varios ejes
    p7a = pc.mulEjes(kx=5 , kz=5)
    p7b = pc.mulEjes(kx=5 , ky=5)
    p7c = pc.mulEjes(ky=5 , kz=5)
    
    # Imprimimos todos los puntos y los resultados de las operaciones
    p3a.imprimir() # Punto suma(2 , 4 , 6)
    p3b.imprimir() # Punto suma(2 , 3 , 4)
    
    p4a.imprimir() # Punto resta(0 , 0 , 0)
    p4b.imprimir() # Punto suma(0 , 1 , 2)
    p5.imprimir() # punto escalado(10 , 20 , 30)
    p6a.imprimir() # eje x modificado (5,1,1)
    p6b.imprimir() # eje y modificado (1,5,1)
    p6c.imprimir() # eje x modificado (1,1,5)
    p7a.imprimir() # eje x modificado (5,1,5)
    p7b.imprimir() # eje y modificado (5,5,1)
    p7c.imprimir() # eje x modificado (5,1,5)
    
    # creamos un vector v1 de prueba
    v1 = VectorHijo("v1" , 3 , 4 , 0 )
    mag = v1.magnitud()
    print(f" Magnitud de v1 = {mag}")

