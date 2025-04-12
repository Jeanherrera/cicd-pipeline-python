# app/calculadora.py
"""Operaciones matemáticas básicas: suma, resta, etc."""


def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b


def restar(a, b):
    """Resta el segundo número al primero."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


def dividir(a, b):
    """Divide el primer número entre el segundo."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
