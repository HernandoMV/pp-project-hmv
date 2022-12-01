from typing import Union
import fire


def add_numbers(
    a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def main():
    fire.Fire(add_numbers)


if __name__ == "__main__":
    main()
