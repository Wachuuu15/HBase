# main.py
from modules.ddl_commands import (
    create_table, list_tables, disable_table, is_enabled, alter_table_add_family,
    load_initial_data, save_data, drop_table, drop_all_tables,describe_table
)

def main():
    # Cargando los datos iniciales
    load_initial_data()

    while True:
        print("\nMenú de Opciones:")
        print("1. Crear nueva tabla")
        print("2. Listar todas las tablas")
        print("3. Deshabilitar una tabla")
        print("4. Verificar si una tabla está habilitada")
        print("5. Añadir familia de columnas a una tabla")
        print("6. Eliminar una tabla")
        print("7. Descripción de tabla")
        print("8. Eliminar todas las tablas")
        print("9. Salir")
        command = input("Seleccione una opción (1-9): ")

        if command == "9":
            print("Guardando datos y saliendo...")
            save_data()
            break
        elif command == "1":
            table_name = input("Ingrese el nombre de la nueva tabla: ")
            create_table(table_name)
        elif command == "2":
            list_tables()
        elif command == "3":
            table_name = input("Ingrese el nombre de la tabla a deshabilitar: ")
            disable_table(table_name)
        elif command == "4":
            table_name = input("Ingrese el nombre de la tabla para verificar si está habilitada: ")
            enabled = is_enabled(table_name)
            print(f"Tabla '{table_name}' está {'habilitada' if enabled else 'deshabilitada'}.")
        elif command == "5":
            table_name = input("Ingrese el nombre de la tabla a modificar: ")
            new_family = input("Ingrese el nombre de la nueva familia de columnas: ")
            alter_table_add_family(table_name, new_family)
        elif command == "6":
            table_name = input("Ingrese el nombre de la tabla a eliminar: ")
            drop_table(table_name)
        elif command == "7":
            describe_table()
        elif command == "8":
            drop_all_tables()
        else:
            print("Opción no reconocida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
