from time import time as t
from time import sleep as s
from random import random as r
 
def timer(func):
    def wrapper(*args, **kwargs):
        t1 = t()
        result = func(*args, **kwargs)
        t2 = t()-t1
        return f"Llamada a la funcion: {func.__name__}, Argumentos: {args}, {kwargs}, Tiempo en ejecutar: {t2}, resultado: {result}"
    return wrapper


@timer
def esperar(tiempo):
    # simulando una funcion con mucho codigo que tarde en ejecutarse
    s(tiempo)
    return "Its done"


@timer
def potenciar_num(base, exponente):
    s(r()*2)
    return r() < 0.2


# print(esperar(1))
print(potenciar_num(20, 50))