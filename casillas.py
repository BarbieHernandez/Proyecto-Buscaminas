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
    
#Se cambia el estado de la casilla para que ya no esté oculta.
    def revelar(self):
        self.oculta = False
    
#Alterna el valor de "marcada" y "dudosa" con el "not", si es True, se convierte en False y viceversa.
    def marcar(self):
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
    
#Evalúa el valor de "self.oculta" y "self.marcada" para decidir que símbolo mostrar.
    def mostrar(self):
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
        return True #Indica que es una mina
    
    def contenido_visible(self): #Utiliza la función del método abstracto.
        return "💣" #Si la casilla no está oculta, se llama a la función "contenido_visible" para mostrar el símbolo de la bomba.

#Se crea la clase hija "CasillaSinMina"
class CasillaSinMina(Casilla):
    def __init__(self, coordenada):
        super().__init__(coordenada) #Llama a los atributos del padre "Casilla"
        self.minasAlrededor = 0 #Contador de minas que hay en las casillas adyacentes
    
    def esMina(self): #Utiliza la función del método abstracto.
        return False #Indica que no hay una mina
    
    def contenido_visible(self): #Utiliza la función del método abstracto.
        return str(self.minasAlrededor) if self.minasAlrededor > 0 else " "