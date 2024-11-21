# Admin_Library
Bookstore manager, detects when you loan and return books depending on the user. The response is stored in JSON to manage the inventory.


## Estructura del Proyecto

- `clases/`
  - `Libro.py`: Contiene la clase `Libro` que representa un libro en la biblioteca.
  - `Usuario.py`: Contiene la clase `Usuario` que representa un usuario de la biblioteca.
- `estado.json`: Archivo JSON que almacena el estado actual de los usuarios y los libros prestados.
- `main.py`: Archivo principal para ejecutar la aplicación.
- `README.md`: Este archivo.
- `requierements.txt`: Archivo que contiene las dependencias del proyecto.

## Clases

### Usuario

La clase `Usuario` representa un usuario de la biblioteca. Tiene los siguientes atributos y métodos:

- `__init__(self, nombre, edad, telefono, email)`: Constructor de la clase.
- `to_dict(self)`: Convierte el objeto `Usuario` a un diccionario.
- `from_dict(data, libros)`: Crea un objeto `Usuario` a partir de un diccionario.

### Libro

La clase `Libro` representa un libro en la biblioteca. Tiene los siguientes atributos y métodos:

- `__init__(self, titulo, autor, paginas, año, editorial)`: Constructor de la clase.

- `to_dict(self)`: Convierte el objeto `Libro` a un diccionario.
- `from_dict(data)`: Crea un objeto `Libro` a partir de un diccionario.
- `guardar_estado(usuarios, libros_prestados)`: Guarda el estado actual de los usuarios y los libros prestados en `estado.json`.
- `cargar_estado(libros)`: Carga el estado actual de los usuarios y los libros prestados desde `estado.json`.

## Uso

Para ejecutar la aplicación, simplemente ejecute el archivo `main.py`

# Admin_Library

Bookstore manager, detects when you loan and return books depending on the user. The response is stored in JSON to manage the inventory.

## Project Structure

- `clases/`
  - `Libro.py`: Contains the `Libro` class that represents a book in the library.
  - `Usuario.py`: Contains the `Usuario` class that represents a user of the library.
- `estado.json`: JSON file that stores the current state of users and loaned books.
- `main.py`: Main file to run the application.
- `README.md`: This file.
- `requierements.txt`: File that contains the project dependencies.

## Classes

### Usuario

The `Usuario` class represents a user of the library. It has the following attributes and methods:

- `__init__(self, nombre, edad, telefono, email)`: Constructor of the class.
- `to_dict(self)`: Converts the `Usuario` object to a dictionary.
- `from_dict(data, libros)`: Creates a `Usuario` object from a dictionary.

### Libro

The `Libro` class represents a book in the library. It has the following attributes and methods:

- `__init__(self, titulo, autor, paginas, año, editorial)`: Constructor of the class.
- `to_dict(self)`: Converts the `Libro` object to a dictionary.
- `from_dict(data)`: Creates a `Libro` object from a dictionary.
- `guardar_estado(usuarios, libros_prestados)`: Saves the current state of users and loaned books in `estado.json`.
- `cargar_estado(libros)`: Loads the current state of users and loaned books from `estado.json`.

## Usage

To run the application, simply execute the `main.py` file:

```sh
python [main.py](http://_vscodecontentref_/1)