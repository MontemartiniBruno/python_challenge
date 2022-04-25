# Eliminar elementos duplicados es un array

def eliminar(a):
    """Funcion que elimina los elementos duplicados

    Args:
        a (array)
    """

    elementos_duplicados = []
    
    for i in a :
        
        if i in elementos_duplicados:
            pass
        else: 
            elementos_duplicados.append(i)
        
    
    print(elementos_duplicados)
    return a

# print(eliminar([4,5,4,6,4,5,7,8,9,9,9,9,9,9]))


def devolver_saludo(name:str):
    print(f'Hola {name} como estas hoy')

print(devolver_saludo('Bruno'))