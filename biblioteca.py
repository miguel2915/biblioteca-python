
import sqlite3

# Nombre de la base de datos
DB_NAME = "biblioteca.db"


# --------------------------------------------------
# CONECTAR CON LA BASE DE DATOS
# --------------------------------------------------

def conectar():
    """Conecta con la base de datos SQLite."""
    return sqlite3.connect(DB_NAME)


# --------------------------------------------------
# CREAR TABLA
# --------------------------------------------------

def crear_tabla():
    """Crea la tabla libros si no existe."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


# --------------------------------------------------
# AGREGAR LIBRO
# --------------------------------------------------

def agregar_libro():
    print("\n--- AGREGAR NUEVO LIBRO ---")

    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")

    while True:
        estado = input("Estado (leído/no leído): ").lower()

        if estado in ["leído", "no leído"]:
            break

        print("Estado inválido. Escribe 'leído' o 'no leído'.")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO libros (titulo, autor, genero, estado)
        VALUES (?, ?, ?, ?)
    """, (titulo, autor, genero, estado))

    conexion.commit()
    conexion.close()

    print("\nLibro agregado correctamente.")


# --------------------------------------------------
# MOSTRAR LIBROS
# --------------------------------------------------

def mostrar_libros():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()

    conexion.close()

    print("\n--- LISTADO DE LIBROS ---")

    if not libros:
        print("No hay libros registrados.")
        return

    for libro in libros:
        print(f"""
ID: {libro[0]}
Título: {libro[1]}
Autor: {libro[2]}
Género: {libro[3]}
Estado: {libro[4]}
-------------------------
""")


# --------------------------------------------------
# BUSCAR LIBROS
# --------------------------------------------------

def buscar_libros():
    print("\n--- BUSCAR LIBROS ---")
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Buscar por género")

    opcion = input("\nSelecciona cómo quieres buscar: ")

    if opcion == "1":
        campo = "titulo"
        nombre_campo = "título"

    elif opcion == "2":
        campo = "autor"
        nombre_campo = "autor"

    elif opcion == "3":
        campo = "genero"
        nombre_campo = "género"

    else:
        print("\nOpción inválida.")
        return

    termino = input(f"Escribe el {nombre_campo} a buscar: ")

    conexion = conectar()
    cursor = conexion.cursor()

    consulta = f"""
        SELECT * FROM libros
        WHERE {campo} LIKE ?
    """

    # Los % permiten buscar solamente una parte del texto
    cursor.execute(consulta, (f"%{termino}%",))

    libros = cursor.fetchall()

    conexion.close()

    if not libros:
        print("\nNo se encontraron libros.")
        return

    print("\n--- RESULTADOS ---")

    for libro in libros:
        print(f"""
ID: {libro[0]}
Título: {libro[1]}
Autor: {libro[2]}
Género: {libro[3]}
Estado: {libro[4]}
-------------------------
""")


# --------------------------------------------------
# ACTUALIZAR LIBRO
# --------------------------------------------------

def actualizar_libro():
    print("\n--- ACTUALIZAR LIBRO ---")

    try:
        id_libro = int(input("ID del libro: "))
    except ValueError:
        print("Debes introducir un número.")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM libros WHERE id = ?",
        (id_libro,)
    )

    libro = cursor.fetchone()

    if libro is None:
        print("No existe un libro con ese ID.")
        conexion.close()
        return

    print("\nDeja vacío un campo para conservar su valor actual.")

    titulo = input(f"Título [{libro[1]}]: ")
    autor = input(f"Autor [{libro[2]}]: ")
    genero = input(f"Género [{libro[3]}]: ")
    estado = input(f"Estado [{libro[4]}]: ").lower()

    if titulo == "":
        titulo = libro[1]

    if autor == "":
        autor = libro[2]

    if genero == "":
        genero = libro[3]

    if estado == "":
        estado = libro[4]

    if estado not in ["leído", "no leído"]:
        print("Estado inválido.")
        conexion.close()
        return

    cursor.execute("""
        UPDATE libros
        SET titulo = ?,
            autor = ?,
            genero = ?,
            estado = ?
        WHERE id = ?
    """, (
        titulo,
        autor,
        genero,
        estado,
        id_libro
    ))

    conexion.commit()
    conexion.close()

    print("\nLibro actualizado correctamente.")


# --------------------------------------------------
# ELIMINAR LIBRO
# --------------------------------------------------

def eliminar_libro():
    print("\n--- ELIMINAR LIBRO ---")

    try:
        id_libro = int(input("ID del libro: "))
    except ValueError:
        print("Debes introducir un número.")
        return

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM libros WHERE id = ?",
        (id_libro,)
    )

    libro = cursor.fetchone()

    if libro is None:
        print("No existe un libro con ese ID.")
        conexion.close()
        return

    print(f"\nLibro encontrado: {libro[1]}")

    confirmacion = input(
        "¿Seguro que deseas eliminarlo? (s/n): "
    ).lower()

    if confirmacion == "s":
        cursor.execute(
            "DELETE FROM libros WHERE id = ?",
            (id_libro,)
        )

        conexion.commit()

        print("Libro eliminado correctamente.")

    else:
        print("Operación cancelada.")

    conexion.close()


# --------------------------------------------------
# MENÚ PRINCIPAL
# --------------------------------------------------

def menu():
    while True:
        print("""
========================================
       SISTEMA DE BIBLIOTECA
========================================

1. Agregar nuevo libro
2. Actualizar información de un libro
3. Eliminar libro
4. Ver listado de libros
5. Buscar libros
6. Salir

========================================
""")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_libro()

        elif opcion == "2":
            actualizar_libro()

        elif opcion == "3":
            eliminar_libro()

        elif opcion == "4":
            mostrar_libros()

        elif opcion == "5":
            buscar_libros()

        elif opcion == "6":
            print("\nPrograma finalizado. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intenta nuevamente.")


# --------------------------------------------------
# INICIO DEL PROGRAMA
# --------------------------------------------------

if __name__ == "__main__":
    crear_tabla()
    menu()
