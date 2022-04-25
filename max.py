from logging import exception


def custom_max(a :int, b:int):
    """Funcion que devuelve el valor máximo entre 2 enteros

    Args:
        a (int): [description]
        b (int): [description]
    """
    if a > b:
        return a
    
    elif b > a:
        return b
    
    else:
        print('Los numeros no pueden ser iguales')


print(custom_max(1,45))
print(custom_max(150,-56))
print(custom_max(45,45))