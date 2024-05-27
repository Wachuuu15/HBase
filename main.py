# main.py
from modules.ddl_commands import create_table, list_tables, load_initial_data

def main():
    # Cargando los datos iniciales desde el módulo ddl_commands
    load_initial_data()
    
    # Listando las tablas para verificar la carga
    list_tables()

if __name__ == "__main__":
    main()
