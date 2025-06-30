from archivoconfiguracion import ArchivoConfiguracion #Todas las clases y funciones de la clase "ArchivoConfiguracion" se importan a este archivo.
from jugador import Jugador #Todas las clases y funciones de la clase "Jugador" se importan a este archivo.
from mejortiempo import MejorTiempo #Todas las clases y funciones de la clase "MejorTiempo" se importan a este archivo.
from tablero import Tablero #Todas las clases y funciones de la clase "Tablero" se importan a este archivo.
import time #El número retornado por "time" se puede convertir a un formato de hora más común.

#Se crea la clase "Juego"
class Juego:
    tamaños = { #Los tamaños del tablero según su dificultad colocados como matricez.
        "1": (8, 8, 10),
        "2": (16, 16, 40),
        "3": (30, 16, 99),
    }
    
    def __init__(self):

        """
        Inicia una nueva instancia de Juego.
        
        """

        self.jugador = None #No está asignado, pero va a estarlo cuando un jugador empieze a jugar.
        self.tablero = None #No está asignado, pero se va a asignar dependiendo de las configuraciones del juego.
        self.estadoJuego = "inicio" #Empieza en inicio
        self.tamaños = { 
            "1": (8, 8, 10),
            "2": (16, 16, 40),
            "3": (30, 16, 99)
        }
        self.tiempoInicio = 0 #Empieza en 0, empezará a contar cuando se inicie el juego.
        self.tiempoFin = 0 #Empieza en 0, cumplrá su función cuando se finalice el juego.
        self.archivo = ArchivoConfiguracion() #Una instancia de "ArchivoConfiguracion" para administrar la configuración del juego.
    
    def iniciar(self):

        """
        Inicia un nuevo juego de Buscaminas.
        
        """

        self.jugador = Jugador(input("Nombre del jugador: ")) #Una instancia para que el jugador ponga su nombre antes de empezar a jugar.
        self.estadoJuego = "jugando" #Actualiza el estado del juego a "jugando".
        self.seleccionarTablero() #Se llama la función "seleccionarTablero" para que el jugador pueda elegir el tablero con el que va a jugar.
        if self.tablero: #Solo si el tablero se creó correctamente.
            self.tiempoInicio = time.time() #Se importa "time" para registrar la hora actual como hora de inicio del juego.
            self.jugar() ##Inicia el bucle principal del juego o proceso de juego.
        else:
            print("No se pudo iniciar el juego sin un tablero válido.")
    
    def seleccionarTablero(self):

        """
        Solicita al jugador que seleccione un tamaño de tablero según el nivel de dificultad que desea.
        
        """

        print("\nSeleccione tamaño de tablero:") #El jugador debe elegir el nivel de dificultad del juego de acuerdo al numero de filas y columnas del tablero.
        print("1. 8x8 (10 minas)") #Nivel de dificultad bajo.
        print("2. 16x16 (40 minas)") #Nivel de dificultad medio.
        print("3. 30x16 (99 minas)") #Nivel de dificultad alto.
        
        opcion = input("Opción: ") #Aquí el jugador podrá seleccionar con qué tablero desea jugar insertando su respectivo número.
        
        if opcion in self.tamaños: #Verifica si la entrada es una clave válida en el diccionario "tamaños".
            filas, columnas, minas = self.tamaños[opcion] #Saca las dimensiones y el recuento de minas.
            self.tablero = Tablero(filas, columnas, minas) #Crea una nueva instancia de "Tablero".
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.") #Error si no se introducen los numeros mencionados anteriormente.
    
    def jugar(self):

        """
        Ejecuta el bucle principal del juego.
        
        """

        while self.estadoJuego == "jugando": #Continúa mientras el estado del juego sea "jugando".
            self.tablero.mostrarTablero() #Muestra el estado actual del tablero al jugador.
            self.procesarAccion() #Maneja la entrada del jugador y actualiza el tablero en consecuencia.
            self.verificarVictoria() #Comprueba si el juego se ha ganado o perdido.
        
        self.mostrarResultados() #Muestra el resultado final del juego (victoria/derrota).
    
    def procesarAccion(self):

        """
        Solicita al jugador una acción (Revelar, Marcar o Salir) y coordina, para luego ejecutar la acción elegida en el tablero de juego.
        
        """
    
        while True: #Bucle para garantizar una entrada de acción válida.
            accion = input("\nAcción (R: Revelar, M: Marcar, , D: Dudosa, S: Salir): ").upper() #"upper()" convierte todos los caracteres de un string en mayúsculas.
        
            if accion == "S": #Si el jugador selecciona S, saldrá del juego.
                self.estadoJuego = "terminado" #Establece el estado del juego en "terminada" si el jugador sale.
                return #Devuelve la función.
            
            try:
                fila = int(input("Fila: ")) - 1 #Obtiene la entrada de fila, resta 1 para registrarlo basado en 0.
                columna = int(input("Columna: ")) - 1 #Obtiene la entrada de la columna, resta 1 para registrarlo basado en 0.
        
                if not (0 <= fila < self.tablero.filas and 0 <= columna < self.tablero.columnas):
                    print("¡Coordenadas fuera del tablero!")
                    continue #Pedir de nuevo
            except ValueError:
                print("¡Entrada inválida! Ingrese números para fila y columna.")
                continue #Pedir de nuevo

            if accion == "R": #Si el jugador selecciona R, revelará una casilla.
                if not self.tablero.revelarCasilla(fila, columna): #Intenta revelar la celda, si es una mina, "revelarCasilla" es False.
                    self.estadoJuego = "perdido" #El jugador revela una mina, perdiendo el juego.
                    break
            elif accion == "M": #Marcar o desmarcar una casilla.
                self.tablero.marcarCasilla(fila, columna) #Se activa o desactiva una bandera para la fila y la columna basadas en 0.
                break 
            elif accion == "D": #Marcar o desmarcar una casilla con una interrogante.
                self.tablero.marcarCasillaDudosa(fila, columna)
                break
            else:
                print("Acción no válida. Por favor, ingrese R, M, D o S.")
                continue # Pedir de nuevo
    
    def verificarVictoria(self):
        
        """
        Comprueba si el jugador ha ganado la partida. Se cumple la condición de victoria cuando se revelan todas las celdas del tablero que no son minas.
        
        """

        celdas_seguras = 0 #Contador de todas las celdas sin minas en el tablero.
        celdas_reveladas = 0 #Contador de celdas seguras reveladas por el jugador.
        
        for fila in self.tablero.casillas: #Itera a través de cada fila y cada celda dentro de la fila.
            for casilla in fila: 
                if not casilla.esMina(): #Comprueba si la celda actual no es una mina.
                    celdas_seguras += 1 #Incrementa el recuento total de celdas seguras.
                    if not casilla.oculta: #Comprueba si la celda segura ha sido revelada.
                        celdas_reveladas += 1 #Incrementa el recuento de celdas seguras reveladas.
        
        if celdas_seguras == celdas_reveladas: #Si se han revelado todas las celdas seguras, el jugador gana.
            self.estadoJuego = "ganado" #Actualiza el estado del juego a "ganado".
            self.tiempoFin = time.time() #Registra la hora exacta en que se ganó el juego.
    
    def mostrarResultados(self):

        """
        Muestra los resultados finales del juego al jugador.
        Muestra el estado final del tablero, indica si el jugador ganó, perdió o abandonó, y muestra el tiempo total jugado.
        
        """

        self.tablero.mostrarTablero() #Muestra el tablero una última vez con el estado final
        
        if self.estadoJuego == "ganado": #Calcula el tiempo total jugado si se ganó el juego.
            tiempo_total = self.tiempoFin - self.tiempoInicio #Se asegura de que los tiempos estén establecidos.
            print(f"\n¡Ganaste! Tiempo: {tiempo_total:.2f} segundos")
            
            if self.es_record(tiempo_total): #Verifica y registra un nuevo registro si corresponde.
                print("¡Nuevo récord!")
                record = MejorTiempo( #Asegura que la clase "MejorTiempo" esté definida y acepte estos argumentos.
                    self.jugador.nombre,
                    tiempo_total,
                    (self.tablero.filas, self.tablero.columnas) #Dimensiones del tablero.
                )
                self.archivo.guardarMejorTiempo(record) #Asegura que "self.archivo" sea una instancia de "ArchivoConfiguracion".
        
        elif self.estadoJuego == "perdido": #Muestra que el jugador perdió después de tocar una mina.
            print("\n¡Perdiste! Has pisado una mina")
        
        self.registrarTiempo() #Registra el tiempo del juego sin importar el resultado.
    
    def es_record(self, tiempo):

        """
        Determina si un tiempo determinado (duración del juego) califica como un nuevo récord para el tamaño actual del tablero.
        
        """

        records = self.archivo.leerMejoresTiempos() #"self.archivo.leerMejoresTiempos()" devuelve una lista de diccionarios.
        if not records: #Si no hay registros, la hora actual se considera automáticamente un registro.
            return True
        
        tamaño_actual = (self.tablero.filas, self.tablero.columnas) #Obtiene las dimensiones del tablero actual para filtrar registros.
        records_filtrados = [ #"tamaño" se convierte en una tupla para su comparación, ya que se carga como una lista desde un archivo JSON.
            r for r in records
            if r.tamaño_tablero == tamaño_actual #Compara las tuplas para comprobar robustez.
        ]
        
        if not records_filtrados: #Si no existen registros para este tamaño de tablero específico, la hora actual es un nuevo registro.
            return True
        
        #Compara la hora actual con la hora mínima entre los registros filtrados. Si la hora actual es menor que la mejor hora existente, se trata de un nuevo registro.
        return tiempo < min(r.tiempo for r in records_filtrados) 

    
    def registrarTiempo(self):

        """
        Lee todos los mejores tiempos existentes, luego los itera e imprime los detalles de los primeros 5 registros, incluyendo el nombre del jugador, el tiempo y las dimensiones del tablero.
        
        """
        
        records = self.archivo.leerMejoresTiempos() #Ordena los registros por tiempo para garantizar que los mejores tiempos se muestren primero.
        records.sort(key=lambda record: record.tiempo)
        for i, record in enumerate(records[:5], 1): #Itera e imprime solo los 5 registros superiores.
            print(f"{i}. {record['nombre']}: {record['tiempo']:.2f}s "
                  f"({record['tamaño'][0]}x{record['tamaño'][1]})")

#Inicia el juego
if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()