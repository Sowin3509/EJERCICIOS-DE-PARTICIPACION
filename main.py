from math import sqrt

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f'Punto: ({self.x}, {self.y})')

    def mover(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        return sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perimetro(self):
        ancho = abs(self.punto2.x - self.punto1.x)
        alto = abs(self.punto2.y - self.punto1.y)
        return 2 * (ancho + alto)

    def calcular_area(self):
        ancho = abs(self.punto2.x - self.punto1.x)
        alto = abs(self.punto2.y - self.punto1.y)
        return ancho * alto

    def es_cuadrado(self):
        ancho = abs(self.punto2.x - self.punto1.x)
        alto = abs(self.punto2.y - self.punto1.y)
        return ancho == alto

from math import pi, sqrt

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * pi * self.radio

    def punto_pertenece(self, punto):
        return self.centro.calcular_distancia(punto) <= self.radio
