from math import pi, sqrt
#PUNTO 1

class Vehiculo:
    def __init__(self,velocidad_maxima, kilometra):
        self.velocidad_maxima = velocidad_maxima
        self.kilometra = kilometra

#PUNTO 2

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

#punto 4

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
        return ancho == alto,

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


class Carta:
    PINTAS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']

    def __init__(self, valor, pinta):
        if pinta not in Carta.PINTAS:
            raise ValueError("Pinta inválida")
        self.valor = valor
        self.pinta = pinta


class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
        else:
            print("Monto inválido o saldo insuficiente.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota

    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: ${self.balance:.2f}")




