import json
import random
from clases.Usuario import Usuario

class Libro:
    def __init__(self, titulo, autor, paginas, año, editorial):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.año = año
        self.editorial = editorial

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'paginas': self.paginas,
            'año': self.año,
            'editorial': self.editorial
        }

    @staticmethod
    def from_dict(data):
        return Libro(data['titulo'], data['autor'], data['paginas'], data['año'], data['editorial'])

    def guardar_estado(usuarios, libros_prestados):
        with open('estado.json', 'w') as f:
            json.dump({
                'usuarios': [usuario.to_dict() for usuario in usuarios],
                'libros_prestados': [libro.titulo for libro in libros_prestados]
            }, f)

    def cargar_estado(libros):
        try:
            with open('estado.json', 'r') as f:
                data = json.load(f)
                usuarios = [Usuario.from_dict(usuario_data, libros) for usuario_data in data['usuarios']]
                libros_prestados = [libro for libro in libros if libro.titulo in data['libros_prestados']]
                return usuarios, libros_prestados
        except FileNotFoundError:
            return [], []
    



