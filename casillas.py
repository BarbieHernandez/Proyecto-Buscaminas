from abc import ABC, abstractmethod

#La clase "Casilla" es una clase base abstracta para el Buscaminas, sirve como un plano para otras clases.
class Casilla(ABC):
    def __init__(self, coordenada):
        self.oculta = True
        self.marcada = False #Son booleans porque representa que Casilla puede tener tres estados.
        self.dudosa = False
        self.coordenada = coordenada #Almacena las casillas.
    
#El "abstractmethod" hace que las clases hijas de Casilla tengan obligatoriamente la función "esMina".
    @abstractmethod
    def esMina(self):
        pass #Todavía no hay implementación (código) solo la declaración.
    
    def revelar(self):
        """
        Cambia el estado de la casilla para que ya no esté oculta.
        
        """
        self.oculta = False
    
    def marcar(self):
        """
        Alterna el valor de "marcada" y "dudosa" con el "not", si es True, se convierte en False y viceversa.
        Este método permite al jugador marcar una casilla como sospechosa de contener una mina
        o dejarla como dudosa si no está seguro. Usa condicionales para alternar entre los tres estados.

        """
        if self.dudosa:
            if not self.marcada and not self.dudosa: #Si no está marcada ni dudosa, se puede poner bandera.
                self.marcada = True
                self.dudosa = False
            elif self.marcada and not self.dudosa: #Si tiene bandera, se puede poner interrogante.
                self.marcada = False
                self.dudosa = True
            elif not self.marcada and self.dudosa: #Si tiene interrogante, se puede quitar.
                self.marcada = False
                self.dudosa = False
    
    def mostrar(self):
        """
        Evalúa el valor de "self.oculta" y "self.marcada" para decidir que símbolo mostrar.
        Si la casilla está oculta:
            - Devuelve 🚩 si está marcada con una bandera.
            - Devuelve ❓ si está marcada como dudosa.
            - Devuelve ⬜ si no tiene ninguna marca.
        Si la casilla está revelada:
            - Devuelve el contenido visible de la casilla (mina, número o espacio).

        """
        if self.oculta: #Si la casilla está oculta, revisa si está marcada con una bandera y devuelve su símbolo, si no, devuelve el cuadro oculto.
            if self.marcada: 
                return "🚩" 
            elif self.dudosa:
                return "❓"
            else:
                return "⬜"
        return self.contenido_visible()
    #Si ya está revelada, no se realiza esta función.
    
#Las clases hijas de "Casilla" tienen que tener obligatoriamente la función "contenido_visible".
    @abstractmethod
    def contenido_visible(self):
        pass #Todavía no hay implementación (código) solo la declaración.

#Se crea la clase hija "CasillaConMina" 
class CasillaConMina(Casilla):
    def esMina(self): #Utiliza la función del método abstracto.
        """
        Indica que es una mina.

        """
        return True 
    
    def contenido_visible(self): #Utiliza la función del método abstracto.
        """
        Si la casilla no está oculta, se llama a la función "contenido_visible" para mostrar el símbolo de la bomba.
    
        """
        return "💣" 

#Se crea la clase hija "CasillaSinMina"
class CasillaSinMina(Casilla):
    def __init__(self, coordenada):
        super().__init__(coordenada) #Llama a los atributos del padre "Casilla"
        self.minasAlrededor = 0 #Contador de minas que hay en las casillas adyacentes
    
    def esMina(self): #Utiliza la función del método abstracto.
        """ 
        Indica que no hay una mina.
        
        """
        return False 
    
    def contenido_visible(self): #Utiliza la función del método abstracto.
        return str(self.minasAlrededor) if self.minasAlrededor > 0 else " "