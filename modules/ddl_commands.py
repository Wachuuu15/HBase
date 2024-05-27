import json

# Este diccionario simulará nuestra "base de datos" con las tablas y sus datos.
tables = {}

def load_initial_data():
    """Carga los datos iniciales desde un archivo JSON."""
    try:
        with open('data/initial_data.json', 'r') as file:
            initial_data = json.load(file)
        for row_key, contents in initial_data.items():
            for family, columns in contents.items():
                if row_key not in tables:
                    tables[row_key] = {}
                tables[row_key][family] = columns
        print("Datos iniciales cargados correctamente.")
    except FileNotFoundError:
        print("Archivo de datos inicial no encontrado.")

def create_table(table_name, column_families):
    """Crea una tabla con las familias de columnas especificadas."""
    if table_name not in tables:
        tables[table_name] = {cf: {} for cf in column_families}  # Crea un diccionario vacío para cada familia de columnas.
        print(f"Tabla '{table_name}' creada con column families {column_families}.")
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
