import requests  # Importa la librería requests

# --- CONFIGURACIÓN DEL JUEGO DESDE LA API ---
url1 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/config.json"

response = requests.get(url1)

if response.status_code == 200:
    datos = response.json()

    tamaño_tablero = datos["global"]["board_size"]
    cantidad_de_minas_facil = datos["global"]["quantity_of_mines"]["easy"]
    cantidad_de_minas_medio = datos["global"]["quantity_of_mines"]["medium"]
    cantidad_de_minas_dificil = datos["global"]["quantity_of_mines"]["hard"]

    print(f"Tamaño del tablero: {tamaño_tablero[0]}x{tamaño_tablero[1]}\n"
          f"-Cantidad de minas: Facil: {cantidad_de_minas_facil} Medio: {cantidad_de_minas_medio} Dificl: {cantidad_de_minas_dificil}")

else:
    print(f"Error al consultar a la api: {response.status_code}")

# --- LEADERBOARD DESDE LA API ---
url2 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/leaderboard.json"

response = requests.get(url2)

if response.status_code == 200:
    datos_ranking = response.json()

    print("\n--- Mejores Tiempos ---")
    if datos_ranking:
        datos_ranking.sort(key=lambda x: x["time"])

        for i, registro in enumerate(datos_ranking[:3]):
            nombre_completo = registro["first_name"], registro["last_name"]
            tiempo_record = registro["time"]

            try:
                tamaño_tablero_record = registro["board_size"]
            except KeyError:
                tamaño_tablero_record = ["?", "?"]

            try:
                dificultad_record = registro["difficulty"]
            except KeyError:
                dificultad_record = "?"

            print(f"{i+1}. {nombre_completo}: {tiempo_record:.2f}s "
                  f"({tamaño_tablero_record[0]}x{tamaño_tablero_record[1]} - {dificultad_record})")
    else:
        print("No hay registros en el leaderboard.")
else:
    print(f"Error al consultar a la API del leaderboard: {response.status_code}")
def mostrar_configuracion_y_leaderboard():
    """
    Muestra la configuración inicial del juego y una tabla de mejores tiempos simulada.
    """
    print("Tamaño del tablero: 8x8")  # Imprime el tamaño base del tablero.
    print("-Cantidad de minas: Facil: 0.1 Medio: 0.3 Dificl: 0.6\n")  # Imprime las proporciones de minas por dificultad.

    print("--- Mejores Tiempos ---")  # Encabezado para la tabla de récords simulados.
    leaderboard = [  # Lista de tuplas con nombre, apellido y tiempo de los jugadores.
        ("Jose", "Quevedo", 15.50),
        ("Antonio", "Guerra", 17.45),
        ("Luis", "Bello", 25.30)
    ]

    for i, (nombre, apellido, tiempo) in enumerate(leaderboard, 1):  # Itera sobre la lista, numerando desde 1.
        print(f"{i}. ({nombre!r}, {apellido!r}): {tiempo:.2f}s (?x? - ?)")  # Imprime cada récord con formato y placeholders para tamaño.
