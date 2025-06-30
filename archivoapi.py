import requests # type: ignore 
#Importa la librería requests

url1 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/config.json" #Link de la primera API.

response = requests.get(url1) #Realiza una petición "get" al primer link. Se almacena en la variable "response".

if response.status_code == 200: #Comprueba si la petición fue exitosa. 
    datos = response.json() #Si la petición fue exitosa, el contenido de la respuesta "json" se convierte en un diccionario "datos".

    tamaño_tablero = datos["global"]["board_size"] #Accede al diccionario datos para extraer el tamaño del tablero. 
    cantidad_de_minas_facil = datos["global"]["quantity_of_mines"]["easy"] #Extrae la cantidad de minas para cada nivel de dificultad de "datos".
    cantidad_de_minas_medio = datos["global"]["quantity_of_mines"]["medium"] 
    cantidad_de_minas_dificil = datos["global"]["quantity_of_mines"]["hard"] 

    #Imprime la información de configuración del tablero y las minas. 
    print(f""" 
    Tamaño del tablero: {tamaño_tablero[0]}x{tamaño_tablero[1]}
    Cantidad de minas: Facil: {cantidad_de_minas_facil} Medio: {cantidad_de_minas_medio} Dificl: {cantidad_de_minas_dificil}

""")
    
else: 
    print(f"Error al consultar a la api: {response.status_code}") #Si la petición no fue exitosa, se imprime un mensaje de error. 

url2 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/leaderboard.json" #Link de la segunda API.

response = requests.get(url2)

if response.status_code == 200:
    datos_ranking = response.json() #Si la petición fue exitosa, el contenido JSON de la respuesta se convierte en una lista de diccionarios. Se le da el nombre datos_ranking para mayor claridad.

    print("\n--- Mejores Tiempos (Leaderboard) ---")
    if datos_ranking: #Verifica si la lista no está vacía.
        #Ordena los registros por tiempo para mostrar los mejores primero.
        datos_ranking.sort(key=lambda x: x["time"])

        #Muestra los primeros 3 registros.
        for i, registro in enumerate(datos_ranking[:3]): #Tomamos los 3 primeros mejores, añade un contador i que empieza en 0.
            nombre_completo = f"{registro['first_name']} {registro['last_name']}" #Concatena el nombre y apellido del jugador.
            tiempo_record = registro['time'] #Extrae el tiempo registrado.
            tamaño_tablero_record = registro['board_size'] #Extrae las dimensiones del tablero en el que se logró el récord.
            dificultad_record = registro['difficulty'] #Extrae la dificultad del juego.

            print(f"{i+1}. {nombre_completo}: {tiempo_record:.2f}s " #Imprime cada registro.
                  f"({tamaño_tablero_record[0]}x{tamaño_tablero_record[1]} - {dificultad_record})")
    else:
        print("No hay registros en el leaderboard.") #Si la lista "datos_ranking" está vacía, se informa que no hay registros.

else:
    print(f"Error al consultar a la API del leaderboard: {response.status_code}") #Si la petición no fue exitosa, se imprime un mensaje de error.
