
def soma(x :int, y: int) -> int:
    """Função de soma."""
    return x + y


def sub(x :int, y: int) -> int:
    """Função de subtração."""
    return x - y

def mult(x :int, y: int) -> int:
    """Função de multiplicação."""
    return x * y


def div(x :int, y: int) -> int:
    """Função de divisão."""
    try:
        return x / y

    except ZeroDivisionError:
        return 'Divisao por zero mal sucedida!!'
