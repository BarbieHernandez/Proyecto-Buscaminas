import requests  #Importa la librería requests.

# --- CONFIGURACIÓN DEL JUEGO DESDE LA API ---
url1 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/config.json" #Link de la primera API.

response = requests.get(url1) #Realiza una solicitud GET a la URL.

if response.status_code == 200: #Verifica si la solicitud fue exitosa.
    datos = response.json() #Si es exitosa, transforma la respuesta a JSON.

    tamaño_tablero = datos["global"]["board_size"] #Extrae el tamaño del tablero.
    cantidad_de_minas_facil = datos["global"]["quantity_of_mines"]["easy"] #Extrae la cantidad de minas para cada nivel de dificultad.
    cantidad_de_minas_medio = datos["global"]["quantity_of_mines"]["medium"]
    cantidad_de_minas_dificil = datos["global"]["quantity_of_mines"]["hard"]

    print(f"Tamaño del tablero: {tamaño_tablero[0]}x{tamaño_tablero[1]}\n" #Imprime la información de configuración del tablero y las minas.
          f"-Cantidad de minas: Facil: {cantidad_de_minas_facil} Medio: {cantidad_de_minas_medio} Dificl: {cantidad_de_minas_dificil}")

else:
    print(f"Error al consultar a la api: {response.status_code}") #Si la solicitud falla, imprime un mensaje de error con el código de estado.

# --- LEADERBOARD DESDE LA API ---
url2 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/leaderboard.json" #Link de la segunda API.

response = requests.get(url2) #Realiza una solicitud GET a la URL.

if response.status_code == 200: #Verifica si la solicitud fue exitosa.
    datos_ranking = response.json() #Si es exitosa, transforma la respuesta a JSON.

    print("\n--- Mejores Tiempos ---") 
    if datos_ranking: #Verifica si hay registros en el leaderboard.
        datos_ranking.sort(key=lambda x: x["time"]) #Ordena los registros por el tiempo de forma ascendente.

        for i, registro in enumerate(datos_ranking[:3]): #Itera sobre los primeros 3 mejores tiempos.
            nombre_completo = registro["first_name"], registro["last_name"]  #Extrae el nombre y apellido del jugador.
            tiempo_record = registro["time"] #Extrae el tiempo registrado.

            try: #Intenta obtener el tamaño del tablero, maneja "KeyError" si no existe.
                tamaño_tablero_record = registro["board_size"]
            except KeyError:
                tamaño_tablero_record = ["?", "?"]

            try: #Intenta obtener la dificultad, maneja "KeyError" si no existe.
                dificultad_record = registro["difficulty"]
            except KeyError:
                dificultad_record = "?"

            print(f"{i+1}. {nombre_completo}: {tiempo_record:.2f}s " #Imprime el registro del leaderboard formateado.
                  f"({tamaño_tablero_record[0]}x{tamaño_tablero_record[1]} - {dificultad_record})")
    else: #Si no hay registros, imprime un mensaje indicándolo.
        print("No hay registros en el leaderboard.") 
else: #Si la solicitud falla, imprime un mensaje de error con el código de estado.
    print(f"Error al consultar a la API del leaderboard: {response.status_code}")

def mostrar_configuracion_y_leaderboard():
    """
    Muestra la configuración inicial del juego y una tabla de mejores tiempos simulada.

    """
    print("Tamaño del tablero: 8x8") #Imprime el tamaño base del tablero.
    print("-Cantidad de minas: Facil: 0.1 Medio: 0.3 Dificl: 0.6\n")  #Imprime las proporciones de minas por dificultad.

    print("--- Mejores Tiempos ---") #Encabezado para la tabla de récords simulados.
    leaderboard = [  #Lista de tuplas con nombre, apellido y tiempo de los jugadores.
        ("Jose", "Quevedo", 15.50),
        ("Antonio", "Guerra", 17.45),
        ("Luis", "Bello", 25.30)
    ]

    for i, (nombre, apellido, tiempo) in enumerate(leaderboard, 1):  #Itera sobre la lista, numerando desde 1.
        print(f"{i}. ({nombre!r}, {apellido!r}): {tiempo:.2f}s (?x? - ?)")  #Imprime cada récord con formato y placeholders para tamaño.
