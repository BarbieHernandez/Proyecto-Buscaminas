from archivoapi import *

class ArchivoConfiguracion:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardarArchivo(self, file):
        """

        Guarda un nuevo objeto "MejorTiempo" en el archivo de récords.


        """
        tablero = input("Tamaño del tablero: ")
        cantidad_de_minas = input("Cantidad de minas en el tablero: ")
        mejores_tiempos = input("Mejores tiempos: ")

        datos = f"\n-Tablero jugado: {tablero}\n-Cantidad de minas del tablero: {cantidad_de_minas}\n- 3 mejores tiempos: {mejores_tiempos}"

        with open(file, "a") as archivo:
            archivo.write(datos)

    file = "registros.txt"
    guardarArchivo(file)

    def leerArchivo(file):
        """

        Lee los récords del archivo JSON y los devuelve como una lista de objetos MejorTiempo.


        """
        try:
            with open(file, "r") as archivo: #Convierte cada diccionario en un objeto.
                registro = archivo.read()
                print(registro)   
        except FileNotFoundError: #Si el archivo no existe, significa que no hay registro todavía.
            print(f"Error al leer el archivo de récords: {file}")
         
    leerArchivo(file)

