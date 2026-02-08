"""
Napisz dekorator, ktory bedzie logowac uzycie funkcji, jej nazwe, argumenty, wynik i czas wykonania

Powinno to printowac
Wywolano funkcje `jakas_funkcja` z parametrami: None, wynik: None, czas: 0.000000s
"""

import logging
import time
t1 = time.time()
time.sleep(1)
t2 = time.time()
print(f"Czas: {t2-t1}s")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename="log.txt")
logger = logging.getLogger(__name__)

def logowanie(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        args_str = None if len(args) == 0 else args
        kwargs_str = None if len(kwargs) == 0 else kwargs

        print(f"Wywolano funkcje `{func.__name__}` z parametrami pozycyjnymi={args_str}, nazwanymi={kwargs_str}, wynik: {result}, czas: {end - start:.6f}s")
        log = f"Wywolano funkcje `{func.__name__}` z parametrami pozycyjnymi={args_str}, nazwanymi={kwargs_str}, wynik: {result}, czas: {end - start:.6f}s"
        logger.info(log)

        return result
    return wrapper

@logowanie
def add(a, b):
    time.sleep(1)
    return a + b

@logowanie
def bar(n=10):
    return sum(x ** n for x in range(n))

add(5, 7)
bar(100)



