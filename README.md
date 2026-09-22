# Biblioteca Personal

## Descripción

Este proyecto consiste en una aplicación de línea de comandos desarrollada en Python para administrar una biblioteca personal.

La aplicación utiliza SQLite para almacenar información sobre libros y permite agregar, consultar, actualizar, eliminar y buscar libros.

## Funcionalidades

El programa cuenta con las siguientes opciones:

1. Agregar nuevo libro.
2. Actualizar información de un libro.
3. Eliminar un libro.
4. Ver listado de libros.
5. Buscar libros.
6. Salir del programa.

## Datos de los libros

Cada libro contiene:

* ID
* Título
* Autor
* Género
* Estado de lectura

El estado de lectura puede ser:

* Leído
* No leído

## Búsqueda

La aplicación permite buscar libros por:

* Título
* Autor
* Género

También permite realizar búsquedas parciales. Por ejemplo, se puede escribir solamente una parte del título, autor o género.

## Tecnologías utilizadas

* Python 3
* SQLite
* Biblioteca `sqlite3`

## Requisitos

Para ejecutar el proyecto se necesita tener instalado Python 3.

No es necesario instalar librerías externas, ya que `sqlite3` viene incluida con Python.

## Instrucciones de ejecución

1. Descargar o clonar el repositorio.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el programa con:

```bash
python biblioteca.py
```

La base de datos `biblioteca.db` se crea automáticamente al ejecutar el programa si todavía no existe.

## Estructura del proyecto

```text
biblioteca-python/
│
├── biblioteca.py
├── biblioteca.db
└── README.md
```

## Base de datos

La aplicación utiliza una base de datos SQLite llamada:

`biblioteca.db`

La información de los libros se almacena en la tabla:

`libros`

## Autor

Proyecto académico desarrollado para practicar la programación en Python y la interacción con bases de datos SQLite.
