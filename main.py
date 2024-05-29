# main.py
from modules.ddl_commands import (
    create_table, list_tables, disable_table, is_enabled, alter_table_add_family,
    load_initial_data, save_data, drop_table, drop_all_tables, describe_table
)

from modules.dml_commands import (
    put, get, scan, delete, delete_all, count, truncate
)

menuDdl= """
1. Crear nueva tabla
2. Listar todas las tablas
3. Deshabilitar una tabla
4. Verificar si una tabla está habilitada
5. Añadir familia de columnas a una tabla
6. Eliminar una tabla
7. Descripción de tabla
8. Eliminar todas las tablas
9. Salir
"""

menuDml= """
1. Insertar dato a la tabla
2. Obtener datos de la tabla
3. Scan
4. Borrar
5. Borrar todo
6. Count
7. Truncate
8. Salir
"""

def main_ddl():
    print("\nMenú DDL (Definición de Datos):")
    while True:
        print("------------------------------------------------------")
        print(menuDdl)
    
        command = input("Seleccione una opción (1-9): ")
        print("------------------------------------------------------")

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
            table_name = input("Ingrese el nombre de la tabla a describir: ")
            describe_table(table_name)
        elif command == "8":
            drop_all_tables()
        else:
            print("Opción no reconocida, por favor intente nuevamente.")

def main_dml():
    print("\nMenú DML (Manipulación de Datos):")
    while True:
        print("------------------------------------------------------")

        print(menuDml)
        command = input("Seleccione una opción (1-8): ")

        print("------------------------------------------------------\n")

        if command == "8":
            print("Guardando datos y saliendo...")
            save_data()
            break

        elif command == "1":
            table_name = input("Ingrese el nombre de la tabla a modificar: ")
            row_key = input("Ingrese el row key: ")
            family_name = input("Ingrese el nombre de la familia de columnas: ")
            column_name = input("Ingrese el nombre de la columna: ")
            value = input("Ingrese el valor a insertar: ")
            put(table_name, row_key, family_name, column_name, value)

        elif command == "2":
            table_name = input("Ingrese el nombre de la tabla: ")
            row_key = input("Ingrese el row key: ")
            family_name = input("Ingrese el nombre de la familia de columnas: ")
            column_name = input("Ingrese el nombre de la columna: ")
            timestamp_input = input("Ingrese el timestamp si desea obtener una versión específica, de lo contrario presione Enter: ")

            timestamp = int(timestamp_input) if timestamp_input.isdigit() else None

            value = get(table_name, row_key, family_name, column_name, timestamp)
            if value is not None:
                print(f"Valor recuperado: {value}")
            else:
                print("No se pudo recuperar ningún valor.")

        elif command == "3":
            print("Ingrese los detalles para escanear la tabla:")
            table_name = input("Nombre de la tabla a escanear: ")
            family_name = input("Nombre de la familia de columnas (presione Enter para omitir): ")
            start_row = input("Row key inicial para el rango de escaneo (presione Enter para omitir): ")
            end_row = input("Row key final para el rango de escaneo (presione Enter para omitir): ")
            scan(table_name, family_name if family_name else None, start_row if start_row else None, end_row if end_row else None)
        
        elif command == "4":
            table_name = input("Ingrese el nombre de la tabla: ")
            row_key = input("Ingrese el row key a eliminar (deje en blanco para borrar toda la fila): ")
            family_name = input("Ingrese la familia de columnas a eliminar (deje en blanco para borrar toda la familia): ")
            column_name = input("Ingrese el nombre de la columna a eliminar (deje en blanco para borrar la columna completa): ")
            delete(table_name, row_key, family_name if family_name else None, column_name if column_name else None)

        elif command == "5":
            table_name = input("Ingrese el nombre de la tabla de la cual borrar todas las filas: ")
            delete_all(table_name)


        elif command == "6":
            table_name = input("Ingrese el nombre de la tabla para contar sus filas: ")
            count(table_name)
        
        elif command == "7":
            table_name = input("Ingrese el nombre de la tabla a truncar: ")
            truncate(table_name)
        else:
            print("Opción no reconocida, por favor intente nuevamente.")


def main():
    load_initial_data()  

    print("\n------------------------------------------------------")
    print("""Seleccione el modo de operación:

    1. DDL (Definición de Datos)
    2. DML (Manipulación de Datos)
    """)

    choice = input("Ingrese su elección (1-2): ")

    if choice == "1":
        main_ddl()
    elif choice == "2":
        main_dml()
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
