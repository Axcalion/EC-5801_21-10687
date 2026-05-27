# definimos una clase base que describa a un dispositivo de memoria
class Memoria:

    def __init__(self , nombreMem:str , N:int):
        self.nombre:str = nombreMem
        # representa el almacenamiento del dispositivo
        # arreglo de tamano N, inicialmente con 0 en todos sus espacios
        self.__mem:list = [0]*N
        # define la velocidad del dispositivo
        self.retraso: int = 0
    
    # Metodo para simular los retrasos de lectura y escritura
    def __delay(self):
        # usamos un bucle vacio para recrear la sensacion de espera
        # mayor retraso implica mas ciclos consumidos
        # a partir de k = 100.000 se siente un retraso "real", lo deje en 10k para poder correr el codigo
        k:int = 10000
        for i in range(self.retraso*k):
            pass
        
    # Metodo para guardar un dato en una posicion de memoria 
    def escribir(self , posicion:int , dato:int):
        # retraso en la reaccion del hardware 
        self.__delay()
        try:
            self.__mem[posicion] = dato
            print(f"[{self.nombre}] escritura en la posicion {posicion}")
        # evita acceso a memoria inexistente
        except(IndexError):
            print(f"[{self.nombre}] posicion fuera de rango")
    
    # Metodo para leer un dato en una posicion especifica de la memoria
    def leer(self , posicion:int ):
        # retraso en la reaccion del hardware simulando una bvusqueda fisica
        self.__delay()
        try:
            valor = self.__mem[posicion]
            print(f"[{self.nombre}] lectura de la posicion {posicion}")
            return valor
        # evita la lectura de memoria inexistente
        except IndexError:
            print(f"[{self.nombre}] posicion no encontrada")
            return None
            


class SSD(Memoria):
    def __init__(self, nombreMem, N):
        super().__init__(nombreMem, N)
        
        # el disco duro es el mas lento en cuanto a funcionamiento real
        self.retraso = 750


class RAM(Memoria):
    def __init__(self, nombreMem, N):
        super().__init__(nombreMem, N)
        
        # definimos un retraso mucho menor debido a que la RAM es mas rapida 
        self.retraso = 50

class SRAM(Memoria): 
    def __init__(self, nombreMem, N):
        super().__init__(nombreMem, N)
        
        # La SRAM (Caché) tiene un tiempo de acceso imperceptible
        self.retraso = 0
        
# Funciones que Simulan un BUS de datos
# Recibe cualquier objeto calse Memoria y guarda un dato.
def busEscribir(dispositivo: 'Memoria', posicion: int, dato: int):
    
    print(f"\n[BUS] Enviando datos a: {dispositivo.nombre}")
    dispositivo.escribir(posicion, dato)

# Recibe cualquier objeto clase Memoria que tenga el metodo .leer() y extrae un dato.
def busLeer(dispositivo: 'Memoria', posicion: int):
    
    print(f"\n[BUS] Accediendo a: {dispositivo.nombre}")
    return dispositivo.leer(posicion)

    print(f"Dato '{valor}' recuperado exitosamente de {dispositivo.nombre}")
    return valor

if __name__ == "__main__":
    # creamos los componentes de hardware con tamanos "equivales" en el orden de megas 
    # SSD = 64Gb , RAM = 2Gb . Cache = 16mb
    discoDuro = SSD("Disco Local C:", 64000)
    ram = RAM("DDR4", 2000)
    sram = SRAM("Caché L1", 16)

    # usamos el bus para escribir un dato en las memorias
    busEscribir(discoDuro, 27, 500)   # Tardará mucho
    busEscribir(ram, 8, 250)     # Tardará poco
    busEscribir(sram, 4, 100)    # Será instantáneo

   # usamos el bus para leer 
    valor_disco = busLeer(discoDuro, 27)
    print(f"Valor recuperado de {discoDuro.nombre}: {valor_disco}")
    
    valor_ram = busLeer(ram, 8)
    print(f"Valor recuperado de {ram.nombre}: {valor_ram}")
    
    valor_sram = busLeer(sram, 4)
    print(f"Valor recuperado de {sram.nombre}: {valor_sram}")