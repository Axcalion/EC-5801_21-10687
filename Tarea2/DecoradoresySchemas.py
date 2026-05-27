# Tarea 2 parte 3
from PyYaml import HijoManager
# Importamos el decorador 
from schema_validator import schema_validator

# definimos el esquema en el formato solicitado
scheme = {
    "nombre": str,
    "altura": float,
    "peso": float,
    "edad": int,
    "lista de habilidades": list,
    "descripcion": str    
}

# definimos la funcion y usamos el decorador en ella
@schema_validator(scheme)
def validarDict(datosValidos: dict):
    return datosValidos

instancia1 = HijoManager()

# funcion de prueba para el esquema
def proof(rutaArchivo: str):

    # carga el archivo usando la clase HijoManager
    datosLeidos = instancia1.cargar(rutaArchivo)
    
    # hace que el decorador revise los datos
    datos = validarDict(datosLeidos)
    
    # alerta si el archivo cumple o no con el esquema 
    if datos is None:
        print(f"El formato del esquema es incorrecto")
        return None
    else: 
        print(f"Archivo YAML procesado correctamente")
        return datos
    
if __name__ == "__main__":
    # Prueba 1, archivo valido"
    proof("campeones.yaml")
    
    # Prueba 2, archivo .text no valido
    proof("campeones.text")
    
    #prueba 3, esquema no valido
    proof("config.yaml")