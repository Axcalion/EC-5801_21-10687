# Tarea 2 parte 1
from pathlib import Path

class FileManager:
    
    def __init__(self):
        pass

    def leerArchivo(self, ruta: str, binario: bool = False):
        # hacemos que la ruta sea de tipo Path
        ruta = Path(ruta)
        
        # verificamos si el archivo es valido
        if ruta.is_file():
        
            # cambiamos el modo de apertura según el tipo de archivo 
            # 'rb' si es archivo binario o 'r' si es texto normal
            if binario:
                modo = 'rb'
            else:
                modo = 'r'    
    
            try:
                # Abre el archivo con la ruta y el modo correcto
                with open(ruta, modo) as archivo:
                    # Lee el contenido del archivo y lo regresa
                    contenido = archivo.read()
                    return contenido
        
            except FileNotFoundError:
                # Alerta si el archivo no existe en el disco
                print(f"[Error] El archivo en la ruta '{ruta}' no fue encontrado.")
                return None 
    
            except Exception as error:
                # avisa de cualquier otro tipo de falla
                print(f"[Error] No se pudo leer el archivo: {error}")
                return None
        else: 
            # alerta en caso de que la verificacion de archivo falle
            print(f"El archivo en '{ruta}' no es valido ")
            return None
            
    def escribirArchivo(self, ruta: str ,  contenido: str | bytes, binario: bool = False ):
        # hacemos que la ruta sea de tipo Path
        ruta = Path(ruta)
        
        # verificamos que la carpeta donde esta el archivo existe
        if ruta.parent.exists():
        
            # cambiamos el modo de escritura según el tipo de archivo 
            # 'wb' si es archivo binario o 'w' si es texto normal
            if binario:
                modo = 'wb'
            else:
                modo = 'w'
        
            try: 
                # abre (o crea) el archivo 
                with open(ruta, modo) as archivo:
                    # escribe la informacion en el archivo
                    archivo.write(contenido)
                    print(f"Archivo guardado correctamente en '{ruta}' ") 
                    return True
        
            except Exception as error:
                # avisa de cualquier otro tipo de falla
                print(f"[Error] No se pudo escribir en el archivo: {error}")
                return False
            
        else:
            # alerta si la carpeta donde se guarda el arvhivo no existe
            print(f"[Error de Ruta] La carpeta para guardar en '{ruta}' no existe.")
            return False
        
        
        