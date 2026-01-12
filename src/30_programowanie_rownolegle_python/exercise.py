import concurrent.futures
import math
import time
from typing import Callable


numbers = list(range(0, 1_00000))


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
        except:
            result = None
        duration = time.time() - start
        print(f"{func.__name__}: {duration:.3f}s")
        return result

    return wrapper


def fun(x: int) -> int:
    y = math.sqrt(x)
    for _ in range(1000):
        y = math.sin(y) + math.cos(y)
    return int(y * 1000)


@timer
def sequential(numbers: list[int], fun: Callable[[int], int]) -> list[int]:
    return [fun(x) for x in numbers]


@timer
def threading(numbers: list[int], fun: Callable[[int], int]) -> list[int]:
    result: list[int] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as e:
        return list(e.map(fun, numbers))

    return result


@timer
def multiprocessing(numbers: list[int], fun: Callable[[int], int]) -> list[int]:
    with concurrent.futures.ProcessPoolExecutor(max_workers=32) as e:
        return list(e.map(fun, numbers))


if __name__ == "__main__":
    sequential(numbers, fun)
    threading(numbers, fun)
    multiprocessing(numbers, fun)
