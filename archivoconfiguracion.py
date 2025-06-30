from mejortiempo import MejorTiempo # Importa la clase MejorTiempo
import json # Necesario para trabajar con JSON

class ArchivoConfiguracion:
    def __init__(self, archivo="records.json"): # Cambiar a .json para indicar el formato
        self.archivo = archivo

    def guardarMejorTiempo(self, nuevo_record_obj):
        """
        Guarda un nuevo objeto MejorTiempo en el archivo de récords.
        Lee los récords existentes, añade el nuevo, los ordena y los reescribe.
        """
        # 1. Leer los récords existentes
        records_list_of_objects = self.leerMejoresTiempos() # Esto devuelve una lista de objetos MejorTiempo

        # 2. Añadir el nuevo récord a la lista
        records_list_of_objects.append(nuevo_record_obj)

        # 3. Ordenar la lista de objetos MejorTiempo por su atributo 'tiempo'
        records_list_of_objects.sort(key=lambda record: record.tiempo)

        # 4. Convertir la lista de objetos MejorTiempo a una lista de diccionarios para guardar en JSON
        records_to_save_as_dicts = [record.to_dict() for record in records_list_of_objects]

        # 5. Escribir la lista de diccionarios en el archivo JSON
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(records_to_save_as_dicts, f, indent=4) # 'indent=4' para un JSON más legible
        except IOError as e:
            print(f"Error: No se pudo guardar el archivo de récords '{self.archivo}'. {e}")

    def leerMejoresTiempos(self):
        """
        Lee los récords del archivo JSON y los devuelve como una lista de objetos MejorTiempo.
        """
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                data_from_json = json.load(f) # Carga el contenido JSON como una lista de diccionarios
                # Convierte cada diccionario en un objeto MejorTiempo
                records_list_of_objects = [MejorTiempo.from_dict(item_dict) for item_dict in data_from_json]
                return records_list_of_objects
        except FileNotFoundError:
            # Si el archivo no existe, significa que no hay récords todavía
            return []
        except json.JSONDecodeError:
            # Si el archivo existe pero su contenido no es un JSON válido
            print(f"⚠️ Atención: El archivo '{self.archivo}' está corrupto o contiene JSON inválido. Se iniciará con una lista de récords vacía.")
            return []
        except Exception as e: # Para capturar cualquier otro error inesperado durante la lectura
            print(f"⚠️ Error inesperado al leer el archivo de récords: {e}")
            return []

