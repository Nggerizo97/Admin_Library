from clases.Usuario import Usuario
from clases.Libro import Libro
import random

def main():
    libros = [Libro('La Odisea', 'Homero', 500, 800, 'Gredos'),
              Libro('La Iliada', 'Homero', 400, 800, 'Gredos'),
              Libro('La Divina Comedia', 'Dante', 700, 1300, 'Gredos'),
              Libro('El Quijote', 'Cervantes', 800, 1600, 'Gredos'),
              Libro('El Aleph', 'Borges', 200, 1950, 'Gredos'),
              Libro('Cien años de soledad', 'García Márquez', 600, 1967, 'Gredos'),
              Libro('La Metamorfosis', 'Kafka', 300, 1915, 'Gredos'),
              Libro('El proceso', 'Kafka', 400, 1925, 'Gredos'),
              Libro('El retrato de Dorian Gray', 'Wilde', 200, 1890, 'Gredos'),
              Libro('El principito', 'Saint-Exupéry', 100, 1990, 'Gredos')]

    usuarios, libros_prestados = Libro.cargar_estado(libros)
    #Usuarios inventados para probar el programa
    if not usuarios:
        usuarios = [Usuario('Juan', 25, 123456789, 'juan289900@gmail.com'),
                    Usuario('Pedro', 30, 987654321, 'pedro289900@gmail.com'),
                    Usuario('Maria', 35, 123456789, 'maria289900@gmail.com'),
                    Usuario('Ana', 40, 987654321, 'ana289900@gmail.com')]

    while True:
        usuario_actual = random.choice(usuarios)
        
        print('Menú')
        print('1. Solicitar préstamo')
        print('2. Devolver libro')
        print('3. Salir')
        opcion = input('Ingrese una opción: ')
        if len(libros) == len(libros_prestados):
            print('No hay libros disponibles')
            break
        elif opcion == '1':
            libros_disponibles = [libro for libro in libros if libro not in libros_prestados]
            if not libros_disponibles:
                print('No hay libros disponibles')
                continue
            print('Libros disponibles:')
            for i, libro in enumerate(libros_disponibles):
                print(f'{i + 1}. {libro.titulo}')
            libro_seleccionado = int(input('Seleccione un libro: '))
            if libro_seleccionado < 1 or libro_seleccionado > len(libros_disponibles):
                print('Libro inválido')
                continue
            libro = libros_disponibles[libro_seleccionado - 1]
            libros_prestados.append(libro)
            usuario_actual.libros_prestados.append(libro)
            print(f'{usuario_actual.nombre} ha prestado el libro {libro.titulo}')
        elif opcion == '2':
            if len(usuario_actual.libros_prestados) == 0:
                print('No tienes libros prestados')
                continue
            print('Tus libros prestados:')
            for i, libro in enumerate(usuario_actual.libros_prestados):
                print(f'{i + 1}. {libro.titulo}')
            libro_seleccionado = int(input('Seleccione un libro: '))
            if libro_seleccionado < 1 or libro_seleccionado > len(usuario_actual.libros_prestados):
                print('Libro inválido')
                continue
            libro = usuario_actual.libros_prestados.pop(libro_seleccionado - 1)
            libros_prestados.remove(libro)
            print(f'{usuario_actual.nombre} ha devuelto el libro {libro.titulo}')
        elif opcion == '3':
            Libro.guardar_estado(usuarios, libros_prestados)
            break

if __name__ == '__main__':
    main()