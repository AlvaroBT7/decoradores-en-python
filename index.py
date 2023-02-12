import time
from random import random
 
def func_info(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()-t1
        return f"Llamada a la funcion: {func.__name__}, Argumentos: {args}, {kwargs}, Tiempo en ejecutar: {t2}, resultado: {result}"
    return wrapper


@func_info
def esperar(tiempo) -> None:
    # simulando una funcion con mucho codigo que tarde en ejecutarse y retornando cualquier garbage para que al formar parte del decorador, la misma funcion muestre su info. Info como... lo que retorna
    time.sleep(tiempo)
    return True


@func_info
def potenciar_num(base, exponente) -> bool:
    # simulando una funcion con mucho codigo que tarde en ejecutarse y retornando cualquier garbage para que al formar parte del decorador, la misma funcion muestre su info. Info como... lo que retorna
    time.sleep(random() * 2)
    return random() < 0.2

@func_info
def print_de_los_chinos(*args) -> str:
    for z in args:
        print(z, end=" ")
    print("")
    return "Todo printeado en pantalla"


print(esperar(1))
print(potenciar_num(20, 50))
print(print_de_los_chinos("vendo", "kebab", "rata"))
print("Its done")