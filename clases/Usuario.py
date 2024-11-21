import json
import random

class Usuario:
    def __init__(self, nombre, edad, telefono, email):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.email = email
        self.libros_prestados = []

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'edad': self.edad,
            'telefono': self.telefono,
            'email': self.email,
            'libros_prestados': [libro.titulo for libro in self.libros_prestados]
        }

    @staticmethod
    def from_dict(data, libros):
        usuario = Usuario(data['nombre'], data['edad'], data['telefono'], data['email'])
        usuario.libros_prestados = [libro for libro in libros if libro.titulo in data['libros_prestados']]
        return usuario
