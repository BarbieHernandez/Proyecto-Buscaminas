#Se crea la clase "MejorTiempo".
class MejorTiempo:
    def __init__(self, nombre_jugador, tiempo, tamaño_tablero): #Se definen los parametros.
        self.nombreJugador = nombre_jugador #Almacena el nombre del jugador.
        self.tiempo = tiempo #Almacena el tiempo en el que jugó.
        self.tamañoTablero = tamaño_tablero #Almacena el tamaño del tablero en el que se realizó el juego.
    
    def mostrar(self): #Muestra el record del jugador.
        return f"{self.nombreJugador}: {self.tiempo:.2f}s ({self.tamañoTablero[0]}x{self.tamañoTablero[1]})"
    #Se inserta el nombre del jugador, el tiempo en el que jugó con dos decimales, y el tamaño del tablero jugado (sus filas y columnas).

    def to_dict(self):
        """
    
        Convierte el objeto "MejorTiempo" a un diccionario para guardar en JSON.
        
        """
        return {
            "nombre": self.nombreJugador,
           "tiempo": self.tiempo,
          "tamano": list(self.tamañoTablero) # Guarda la tupla como lista para JSON.
        }
    
