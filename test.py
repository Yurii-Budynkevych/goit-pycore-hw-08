from typing import TypeVar

T = TypeVar("T", int, str, float)


def calculator(x: T, y: T) -> T:
    return x + y


print(calculator(3, 2))
print(calculator("Hello", "World"))
print(calculator(3.5, 1.4))
