# Tarea 2 parte 2 PyYAML
import yaml 
from pathlib import Path
from Manejo_de_Archivos import FileManager   

class HijoManager(FileManager):
        
    def __init__(self):
        super().__init__()
        # creamos el diccionario
        self.__file = {}
    
    # Metodo para cargar informacion en un diccionario    
    def cargar(self, ruta: str):
            
        # usamos el metedo heredado para leer el archivo
        contenido = self.leerArchivo(ruta)
            
        # alerta si la ruta falla o hay un error al leer
        if contenido is None: 
            print(f"No se pudo leer el archivo")
            return None
            
        # transforma el texto en un diccionario 
        try: 
            diccionario = yaml.safe_load(contenido)
            fileName = Path(ruta).name
            self.__file[fileName] = {
                    "path": str(ruta) ,
                    "data": diccionario
                }                
            print(f"Archivo YAML procesado correctamente")
            return diccionario
            
        # qlerta si el archivo YAML tiene un error de formato (espacios, puntos, etc.)
        except yaml.YAMLError as error_yaml:
            print(f"El formato del YAML es incorrecto: {error_yaml}")
            return None 
            
        # alerta de cualquier otro error 
        except Exception as error:
            print(f"Ha ocurrido un error inesperado: {error}")
            return None
        
    # Metodo GETTER para recuperar la información del diccionario privado   
    def obtener(self, fileName: str):
        
        # verificamos que el archivo esta registrado en el diccionario    
        if fileName in self.__file:
            # si esta registrado, devolvemos la estructura del archivo
            return self.__file[fileName]
        
        else: 
            # alerta si NO esta registrado
            print(f"El archivo '{fileName}' no esta en el sistema")
            return None
        
    # Metodo para MODIFICAR un diccionario    
    def modificar(self, fileName: str, nuevoDiccionario: dict):
        # verificamos qque el archivo existe en el diccionario privado
        if fileName in self.__file:
            # reemplazamos los datos internos sin modificar la ruta
            self.__file[fileName]["data"] = nuevoDiccionario
            print(f"El diccionario asociado a '{fileName}' ha sido modificado")
            return True        
        
        else:
            # alerta si el archivo a modificar no esta cargado
            print(f"El archivo '{fileName}' no esta en el sistema" )
        
    # Metodo para GUARDAR los valores modificados en el disco
    def guardar(self, fileName:str ,):
        # verificamos qque el archivo existe en el diccionario privado
        if fileName in self.__file:
            # extraemos la ruta y los datos del archivo
            rutaArchivo = self.__file[fileName]["path"]
            datosDicc   = self.__file[fileName]["data"]
            
            try:
                # convertimos el diccionario en texto con formato YAML
                contenidoYaml = yaml.dump(datosDicc, default_flow_style = False)
                
                # usamos el metodo 'escribirArchivo' de FileManager para escribir el contenido en el disco duro
                guardado = self.escribirArchivo(rutaArchivo, contenidoYaml)
                return guardado 
            
            # alerta si la escritura o la conversion a YAML fallan
            except Exception as error:
                print(f"No se pudo guardar el archivo modificado: {error}")
                return False
        
        # alerta si se intenta guardar un archivo que no existe   
        else: 
            print(f"El archivo '{fileName}' no esta registrado en el sistema")
            return False       
            
if __name__ == "__main__":
    
    
    ...