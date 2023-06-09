# тікаю з міста
def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
        return cache[key]

    return wrapper


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    print(f'Вызвана функция circle_area с аргументом {r}')
    return 3.14 * (r ** 2)


print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))
print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))
print('Результат выполнения circle_area(20):', circle_area(20))
print('Результат выполнения triangle_area(10, 10):', triangle_area(10, 10))
print('Результат выполнения circle_area(20):', circle_area(20))
print('Результат выполнения circle_area(20):', circle_area(2080))
