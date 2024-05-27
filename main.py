# main.py
import json
from modules.ddl_commands import create_table, list_tables, load_initial_data

def load_initial_data():
    """Carga los datos iniciales desde un archivo JSON."""
    with open('data/initial_data.json', 'r') as file:
        data = json.load(file)
    return data

def main():
    data = load_initial_data()
    
    # Creando las tablas basadas en los datos cargados
    for row_key, contents in data.items():
        for family, columns in contents.items():
            print(f"Procesando {row_key} con familia {family}")

    
    load_initial_data()
    
    list_tables()

if __name__ == "__main__":
    main()
