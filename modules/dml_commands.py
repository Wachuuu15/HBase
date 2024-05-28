# dml_commands.py
import json

tables = {}
from ddl_commands import disable_table, is_enabled

def put(table_name, row_key, family_name, column_name, value, timestamp=None):
    """Inserta o actualiza un valor en una tabla específica."""
    if table_name not in tables:
        print(f"Error: La tabla '{table_name}' no existe.")
        return

    if family_name not in tables[table_name]:
        tables[table_name][family_name] = {}
    
    if row_key not in tables[table_name][family_name]:
        tables[table_name][family_name][row_key] = {}
    
    if column_name not in tables[table_name][family_name][row_key]:
        tables[table_name][family_name][row_key][column_name] = {}

    if not timestamp:
        current_versions = tables[table_name][family_name][row_key][column_name]
        if current_versions:
            latest_version = max(current_versions.keys()) 
            timestamp = latest_version + 1
        else:
            timestamp = 1 

    tables[table_name][family_name][row_key][column_name][timestamp] = value
    print(f"Dato insertado/actualizado en {table_name} -> {family_name}[{row_key}][{column_name}] con versión {timestamp}")

def get(table_name, row_key, family_name, column_name, timestamp=None):
    """Recupera un valor específico de una tabla."""
    try:
        if table_name not in tables:
            raise KeyError(f"La tabla '{table_name}' no existe.")
        if family_name not in tables[table_name]:
            raise KeyError(f"La familia de columnas '{family_name}' no existe en la tabla '{table_name}'.")
        if row_key not in tables[table_name][family_name]:
            raise KeyError(f"El row key '{row_key}' no existe en la familia '{family_name}'.")
        if column_name not in tables[table_name][family_name][row_key]:
            raise KeyError(f"La columna '{column_name}' no existe en el row key '{row_key}'.")

        # Devolver la versión especificada o la más reciente
        cell_data = tables[table_name][family_name][row_key][column_name]
        if timestamp:
            if timestamp in cell_data:
                return cell_data[timestamp]
            else:
                raise KeyError(f"No existe un valor para el timestamp '{timestamp}' en la columna '{column_name}'.")
        else:
            latest_timestamp = max(cell_data.keys())
            return cell_data[latest_timestamp]
    except KeyError as e:
        print(f"Error: {e}")
        return None

def scan(table_name, family_name=None, start_row=None, end_row=None):
    """Escanea y muestra filas de una tabla desde start_row hasta end_row, opcionalmente filtrado por familia de columnas."""
    if table_name not in tables:
        print(f"Error: La tabla '{table_name}' no existe.")
        return
    
    print(f"Datos de la tabla '{table_name}':")
    for row_key in sorted(tables[table_name]):
        if (start_row and row_key < start_row) or (end_row and row_key > end_row):
            continue  # Filtra las row keys que no están en el rango especificado
        
        if family_name and family_name not in tables[table_name][row_key]:
            continue  # Si se especifica una familia y no está en la row key, salta esta iteración

        print(f"Row Key: {row_key}")
        families = [family_name] if family_name else tables[table_name][row_key].keys()
        for fam in families:
            print(f"  Familia de Columnas: {fam}")
            for column, versions in tables[table_name][row_key][fam].items():
                print(f"    Columna: {column}")
                for timestamp, value in versions.items():
                    print(f"      Timestamp: {timestamp}, Valor: {value}")


def delete(table_name, row_key, family_name=None, column_name=None):
    """Elimina una celda o fila específica en una tabla."""
    try:
        if table_name not in tables:
            raise KeyError(f"La tabla '{table_name}' no existe.")
        if row_key not in tables[table_name]:
            raise KeyError(f"El row key '{row_key}' no existe en la tabla '{table_name}'.")
        if family_name:
            if family_name not in tables[table_name][row_key]:
                raise KeyError(f"La familia de columnas '{family_name}' no existe en el row key '{row_key}'.")
            if column_name:
                if column_name not in tables[table_name][row_key][family_name]:
                    raise KeyError(f"La columna '{column_name}' no existe en la familia de columnas '{family_name}'.")
                del tables[table_name][row_key][family_name][column_name]
                print(f"Columna '{column_name}' eliminada.")
            else:
                del tables[table_name][row_key][family_name]
                print(f"Familia de columnas '{family_name}' eliminada.")
        else:
            del tables[table_name][row_key]
            print(f"Row key '{row_key}' eliminado de la tabla '{table_name}'.")
    except KeyError as e:
        print(f"Error: {e}")

def delete_all(table_name):
    """Elimina todas las filas de una tabla específica."""
    if table_name in tables:
        tables[table_name].clear()
        print(f"Todas las filas de la tabla '{table_name}' han sido eliminadas.")
    else:
        print(f"Error: La tabla '{table_name}' no existe.")

def count(table_name):
    """Cuenta el número de filas en una tabla específica."""
    if table_name in tables:
        row_count = len(tables[table_name])
        print(f"Número de filas en la tabla '{table_name}': {row_count}")
        return row_count
    else:
        print(f"Error: La tabla '{table_name}' no existe.")
        return 0
def truncate(table_name):
    """Trunca una tabla, eliminando todas sus filas y recreándola vacía."""
    if table_name in tables:
        print(f"Truncando la tabla '{table_name}'...")
        print("Paso 1: Deshabilitar la tabla")
        disable_table(table_name)  
        print("Paso 2: Eliminar todos los datos de la tabla")
        tables[table_name].clear()  
        print("Paso 3: Habilitar la tabla")
        # Aquí se asume que la tabla simplemente puede ser habilitada de nuevo fácilmente
        # Dependiendo de cómo esté implementado, podría necesitar un paso explícito para habilitar
        is_enabled(table_name)  # Asumiendo que existe una función para habilitar
        print(f"La tabla '{table_name}' ha sido truncada y está lista para ser utilizada de nuevo.")
    else:
        print(f"Error: La tabla '{table_name}' no existe.")

def save_data():
    """Guarda los datos actuales en un archivo JSON."""
    with open('data/current_data.json', 'w') as file:
        json.dump(tables, file, indent=4)
    print("Datos guardados correctamente.")
