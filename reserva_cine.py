butacas = [ ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X']]


def mostrar_asientos(b):
    filas = 4
    columnas = 5

    for i in range(0,filas):
        for j in range(0,columnas):
            if j == columnas-1:
                print(b[i][j])
            else:    
                print(b[i][j], end= " ")



def reserva(n1:int, n2:int):
    """Para realizar una reserva esta funcion recibe el numero de fila y de columna
    Args:
        n1 (int): [description]
        n2 (int): [description]
    """ 
    
    if butacas[n1-1][n2-1] == 'X':
        butacas[n1-1][n2-1] = 'O'
        print(f'Su reserva fue realizada en la fila {n1} asiento {n2}')
        mostrar_asientos(butacas)

    elif butacas[n1-1][n2-1] == 'O':
        print('No se pudo realizar la reserva, el asiento no está disponible')


def inicio():
    print('Bienvenido')
    print('  ')
    mostrar_asientos(butacas)
    print('  ')
    
    while True:
        fila=int(input('Ingrese el numero de fila: '))
        columna=int(input('Ingrese el numero de columna: '))
        reserva(fila,columna)
        print('  ')

        c = input('¿ Desea realizar otra reserva ? (S/N)').upper()
        if c == 'N':
            break
        elif c == 'S':
            pass
        else:
            print('Respuesta invalida')


if __name__ == '__main__':
    inicio()
