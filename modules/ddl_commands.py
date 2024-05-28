import json

# Este diccionario simulará nuestra "base de datos" con las tablas.
tables = {}

def load_initial_data():
    """Carga los datos iniciales desde un archivo JSON."""
    try:
        with open('data/initial_data.json', 'r') as file:
            initial_data = json.load(file)
        for table_name, table_data in initial_data.items():
            create_table(table_name)
            for row_key, contents in table_data.items():
                for family, columns in contents.items():
                    if family not in tables[table_name]:
                        tables[table_name][family] = {}
                    tables[table_name][family][row_key] = columns
        print("Datos iniciales cargados correctamente.")
    except FileNotFoundError:
        print("Archivo de datos inicial no encontrado.")


def create_table(table_name):
    """Crea una tabla vacía para almacenar datos."""
    if table_name not in tables:
        tables[table_name] = {}
        print(f"Tabla '{table_name}' creada.")
    else:
        print(f"Error: La tabla '{table_name}' ya existe.")


def list_tables():
    """Lista todas las tablas disponibles."""
    if tables:
        print("Tablas disponibles:")
        for table_name in tables:
            print(f" - {table_name}")
    else:
        print("No hay tablas disponibles.")


def disable_table(table_name):
    """Deshabilita una tabla especificada."""
    if table_name in tables:
        tables[table_name]['enabled'] = False
        print(f"Tabla '{table_name}' ha sido deshabilitada.")
    else:
        print(f"Error: La tabla '{table_name}' no existe.")


def is_enabled(table_name):
    """Verifica si una tabla está habilitada."""
    if table_name in tables:
        if 'enabled' not in tables[table_name]:
            tables[table_name]['enabled'] = True  # Asumimos que por defecto todas las tablas están habilitadas
        return tables[table_name]['enabled']
    else:
        print(f"Error: La tabla '{table_name}' no existe.")
        return False
    
    
def save_data():
    """Guarda los datos actuales en un archivo JSON."""
    with open('data/current_data.json', 'w') as file:
        json.dump(tables, file, indent=4)
    print("Datos guardados correctamente.")
