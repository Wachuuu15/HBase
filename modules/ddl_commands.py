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
