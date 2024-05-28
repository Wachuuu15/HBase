import pandas as pd
import json
import os

# Cargar los datos del CSV
df = pd.read_csv('netflix_titles2.csv')

# Verificar si la carpeta 'data' existe, si no, crearla
if not os.path.exists('data'):
    os.makedirs('data')

# Función para manejar valores faltantes
def get_value_or_na(value):
    return str(value) if not pd.isnull(value) else "NA"

# Transformar los datos a la estructura JSON deseada
data_json = {"Movie": {}, "TV Show": {}}

for index, row in df.iterrows():
    category = "Movie" if row['type'] == "Movie" else "TV Show"
    
    data_json[category][row['show_id']] = {
        "title": {
            "Timestamp1": get_value_or_na(row['title'])
        },
        "Details": {
            "Type": {"Timestamp1": get_value_or_na(row['type'])},
            "Duration": {"Timestamp1": get_value_or_na(row['duration'])},
            "Rating": {"Timestamp1": get_value_or_na(row['rating'])},
            "Listed in": {"Timestamp1": get_value_or_na(row['listed_in'])},
            "Description": {"Timestamp1": get_value_or_na(row['description'])}
        },
        "Dates": {
            "Date added": {"Timestamp1": get_value_or_na(row['date_added'])},
            "Release year": {"Timestamp1": get_value_or_na(row['release_year'])}
        },
        "People": {
            "Director": {"Timestamp1": get_value_or_na(row['director'])},
            "Cast": {"Timestamp1": get_value_or_na(row['cast'])}
        }
    }

# Guardar el resultado en un archivo JSON dentro de la carpeta 'data'
json_path = os.path.join('data', 'output.json')
with open(json_path, 'w') as json_file:
    json.dump(data_json, json_file, indent=4)

print("El archivo JSON ha sido creado con éxito en la carpeta 'data'.")
