import json #Permite trabajar con archivos JSON.
from mejortiempo import MejorTiempo  #Importa la clase que representa un récord de tiempo.
from archivoapi import * #Todo lo que esté en el archivo "archivoapi" se importa en este archivo.

class ArchivoConfiguracion: #Maneja la lectura y escritura de un archivo de registro.
    def __init__(self, archivo):
        self.archivo = archivo #El nombre del archivo de registros.

    def guardarArchivo(self, file):
        """
        Captura entradas de texto del usuario y las añade al archivo como una cadena de texto simple.

        """
        tablero = input("Tamaño del tablero: ")
        cantidad_de_minas = input("Cantidad de minas en el tablero: ")
        mejores_tiempos = input("Mejores tiempos: ") 

        #Formatea los datos para que sean escritos en el archivo.
        datos = f"\n-Tablero jugado: {tablero}\n-Cantidad de minas del tablero: {cantidad_de_minas}\n- 3 mejores tiempos: {mejores_tiempos}"

        with open(file, "a") as archivo: #Abre el archivo en modo de añadido ('a'). 
            archivo.write(datos) #Escribe los datos en el archivo.

    file = "registros.txt" #Se le otorga el nombre "registros.txt" a "file"
    guardarArchivo(file) #Llama a la función.

    def leerArchivo(file):
        """
        Lee y muestra los registros del archivo especificado.

        """
        try:
            with open(file, "r") as archivo: #Abre el archivo en modo de lectura ('r').
                registro = archivo.read() #Lee lo que hay en el archivo poniéndole el nombre "registro".
                print(registro) #Se imprime "registro".
        except FileNotFoundError: #Si el archivo no existe, significa que no hay registro todavía.
            print(f"Error al leer el archivo de récords: {file}") 
    leerArchivo(file) #Llama a la función.

    def guardarMejorTiempo(self, mejor_tiempo):
        """
        Guarda un nuevo objeto "MejorTiempo" en un archivo JSON llamado "mejores_tiempos.json".
        Si el archivo no existe, lo crea. Si ya existe, añade el nuevo récord a la lista.

        """
        try:
            with open("mejores_tiempos.json", "r") as archivo:
                datos = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            datos = []

        datos.append(mejor_tiempo.to_dict())  # Convierte el objeto a diccionario y lo añade.

        with open("mejores_tiempos.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)  # Guarda la lista actualizada con formato legible.

    def leerMejoresTiempos(self):
        """
        Lee los mejores tiempos desde el archivo "mejores_tiempos.json" y devuelve una lista de objetos "MejorTiempo".
        Si el archivo no existe o está vacío, devuelve una lista vacía.

        """
        try:
            with open("mejores_tiempos.json", "r") as archivo:
                datos = json.load(archivo)
                return [
                    MejorTiempo(
                        record["nombre"],
                        record["tiempo"],
                        tuple(record["tamano"])  # Convierte la lista de vuelta a tupla.
                    )
                    for record in datos
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            return []  