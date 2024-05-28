# dml_commands.py
import json

tables = {}

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


def save_data():
    """Guarda los datos actuales en un archivo JSON."""
    with open('data/current_data.json', 'w') as file:
        json.dump(tables, file, indent=4)
    print("Datos guardados correctamente.")
