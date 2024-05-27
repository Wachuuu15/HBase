# main.py
from modules.ddl_commands import create_table

def main():
    # Ejemplo de creación de tabla
    create_table("students", ["info", "grades"])
    print("Tabla creada exitosamente.")

if __name__ == "__main__":
    main()
