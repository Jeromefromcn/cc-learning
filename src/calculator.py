def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # simple product
    return a * b


def divide(a, b):
    # guard against ZeroDivisionError with a clearer message
    if b == 0:
        raise ValueError("division by zero")
    return a / b
