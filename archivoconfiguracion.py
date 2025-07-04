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
