import requests # type: ignore

url1 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/config.json"

response = requests.get(url1)

if response.status_code == 200:
    datos = response.json()

    tamaño_tablero = datos["global"]["board_size"]
    cantidad_de_minas_facil = datos["global"]["quantity_of_mines"]["easy"] 
    cantidad_de_minas_medio = datos["global"]["quantity_of_mines"]["medium"] 
    cantidad_de_minas_dificil = datos["global"]["quantity_of_mines"]["hard"] 

    print(f"""
    Tamaño del tablero: {tamaño_tablero[0]}x{tamaño_tablero[1]}
    Cantidad de minas: Facil: {cantidad_de_minas_facil} Medio: {cantidad_de_minas_medio} Dificl: {cantidad_de_minas_dificil}

""")
    
else: 
    print(f"Error al consultar a la api: {response.status_code}")

url2 = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/leaderboard.json"

response = requests.get(url2)

if response.status_code == 200:
    datos_ranking = response.json() # Renombrado para claridad

    print("\n--- Mejores Tiempos (Leaderboard) ---")
    if datos_ranking: # Verificar si la lista no está vacía
        # Ordenar los registros por tiempo para mostrar los mejores primero
        datos_ranking.sort(key=lambda x: x["time"])

        # Mostrar los primeros 5 registros (o la cantidad que desees)
        for i, registro in enumerate(datos_ranking[:5]): # Tomamos los 5 primeros
            nombre_completo = f"{registro['first_name']} {registro['last_name']}"
            tiempo_record = registro['time']
            tamaño_tablero_record = registro['board_size']
            dificultad_record = registro['difficulty']

            print(f"{i+1}. {nombre_completo}: {tiempo_record:.2f}s "
                  f"({tamaño_tablero_record[0]}x{tamaño_tablero_record[1]} - {dificultad_record})")
    else:
        print("No hay registros en el leaderboard.")

else:
    print(f"Error al consultar a la API del leaderboard: {response.status_code}")
