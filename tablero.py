#Todas las clases y funciones de la clase "Casilla" se importan a este archivo.
from casillas import *
#Usamos el import random para que los numeros que esten en las casillas sean aleatorios.
import random

#Se crea la clase "Tablero"
class Tablero:
    def __init__(self, filas, columnas, minas_totales):
        self.filas = filas #Almacema cuantas filas tendra el tablero.
        self.columnas = columnas #Almacena cuantas columnas tendra el tablero.
        self.minasTotales = minas_totales #Almacena cuantas minas tendra el tablero. 
        self.casillas = [] #Se crea una lista vacía que será una matriz para almacenas los objetos que estén en "Casilla".
        self.generarTablero() 
    
    def generarTablero(self):
        """

        Prepara el tablero.
        
        
        """
        self.casillas = [ #Se crean casillas vacías
            [CasillaSinMina((f, c)) for c in range(self.columnas)] #Se crea la matriz, se llena con un objeto "CasillaSinMina" y se le pasa su coordenada.
            for f in range(self.filas)
        ]
        
        minas_colocadas = 0 #Se colocan las minas aleatorias 
        while minas_colocadas < self.minasTotales: #Se ejecuta este ciclo hasta que se haya colocado el número deseado de minas.
            #Se elige una fila aleatoria dentro de los límites del tablero.
            fila = random.randint(0, self.filas-1) #Usamos el "random" para que los numeros que esten en las casillas sean aleatorios.
            #Se elige una columna aleatoria dentro de los límites del tablero.
            columna = random.randint(0, self.columnas-1)
            
            if not self.casillas[fila][columna].esMina(): #Se verifica si la casilla seleccionada ya tiene una mina.
                self.casillas[fila][columna] = CasillaConMina((fila, columna)) #Si no tiene mina, se reemplaza el objeto "CasillaSinMina" que estaba allí por un nuevo objeto "CasillaConMina" en esa posición.
                minas_colocadas += 1 #Contador de minas, el cual va incrementando.
        
        #Calcular minas adyacentes.
        for fila in range(self.filas): #Se recorre todo el tablero ahora con las minas puestas.
            for columna in range(self.columnas):
                if not self.casillas[fila][columna].esMina(): #Si no hay minas en una casilla, se llama al método "self.contarMinasAlrededor()" para calcular cuántas minas hay en sus casillas vecinas.
                    self.casillas[fila][columna].minasAlrededor = self.contarMinasAlrededor(fila, columna)
    
    def contarMinasAlrededor(self, fila, columna):
        """
        
        Calcula cuántas minas hay en las ocho casillas que tiene rodean una casilla seleccionada.

        
        """
        count = 0 #Contador de las minas adyacentes.
        #Se recorren las filas y columnas adyacentes de la casilla actual.
        for f in range(max(0, fila-1), min(self.filas, fila+2)): #Se asegura que el bucle no se salga de los límites del tablero.
            for c in range(max(0, columna-1), min(self.columnas, columna+2)): 
                if (f != fila or c != columna) and self.casillas[f][c].esMina(): #No se cuenta la propia casilla si se está verificando. Asegura que solo se cuenten los vecinos.
                #Si la casilla vecina es una mina, se incrementa el contador.
                    count += 1
        return count #Devuelve el total de minas encontradas alrededor de la casilla.
    
    def revelarCasilla(self, fila, columna):
        """
        
        Revela tanto la casilla como las casillas a su alrededor si no tienen minas.
        
        """
        casilla = self.casillas[fila][columna] #Da el objeto "Casilla" en la posición indicada.
        #Si la casilla ya no está oculta (revelada) o si la casilla está marcada con una bandera, la función return termina sin hacer nada. 
        if not casilla.oculta or casilla.marcada or casilla.dudosa: 
            return 
        
        casilla.revelar() #Si la casilla es válida para revelar, llama al método "revelar()" de la propia casilla para cambiar su estado a no oculta.
        
        if casilla.esMina(): #Si la casilla revelada es una mina, el juego termina.
            return False
        
        #Revelar adyacentes si no hay minas alrededor
        if casilla.minasAlrededor == 0: #Si la casilla revelada no tiene minas a su alrededor (espacio en blanco), el juego automáticamente debe revelar sus casillas adyacentes.
            for f in range(max(0, fila-1), min(self.filas, fila+2)): #Se asegura que el bucle no se salga de los límites del tablero.
                for c in range(max(0, columna-1), min(self.columnas, columna+2)):
                    self.revelarCasilla(f, c) #Llama a "revelarCasilla" recursivamente para cada casilla vecina. 
        
        return True #Si la casilla se reveló con éxito y no era una mina, el juego continúa.
    
    def marcarCasilla(self, fila, columna): 
        """
        
        Permite al jugador marcar una casilla.

        
        """
        self.casillas[fila][columna].marcar() #Obtiene la casilla en la posición dada y llama a su método "marcar()", el cual alterna su estado marcada.

    def marcarCasillaDudosa(self, fila, columna):
        """
        
        Permite al jugador marcar una casilla con una interrogante.
        
        
        """
        self.casillas[fila][columna].marcar()
    
    def mostrarTablero(self): 
        """
        
        Muestra cómo va la jugada del usuario.
        
        
        """
        for fila in self.casillas: #Itera sobre cada fila del tablero.
            #Para cada casilla en la fila actual, llama a su método "mostrar()" y devuelve ⬜, 🚩, 💣, número o " ".
            print(" ".join(casilla.mostrar() for casilla in fila)) #"Join" une todos esos símbolos en una sola cadena, separados por un espacio, para formar una línea del tablero.