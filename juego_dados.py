from random import randint


def lanzar_dados():
    return randint(1,6)

def inicio():
    
    print('DADOS GAME')
    print('')

    jugador1 = input('Ingrese nombre del jugador 1: ')
    jugador2 = input('Ingrese nombre del jugador 2: ')

    partidas = 0
    resultados = {jugador1: 0, jugador2:0}

    while True:
        objetivo = lanzar_dados()
        print(f'El objetivo de esta partida es obtener {objetivo}')
        print('')

        input(f'{jugador1} pulse ENTER para lanzar los dados')
        print('')
        
        dado1 = lanzar_dados()
        dado2 = lanzar_dados()

        print(f'Sacaste {dado1} y {dado2}')
        print('')
        if dado1 + dado2 == objetivo:
            print('GANASTE!')
            print('')
            resultados[jugador1] += 1
        
        input(f'{jugador2} pulse ENTER para lanzar los dados')
        print('')
        
        dado1 = lanzar_dados()
        dado2 = lanzar_dados()

        print(f'Sacaste {dado1} y {dado2}')
        print('')
        if dado1 + dado2 == objetivo:
            print('GANASTE!')
            print('')
            resultados[jugador2] += 1
        
        partidas += 1

        c = input(f'Van {partidas} partidas jugadas, desea continuar ? s/n').lower()
        if c == 's':
            pass
        else:
            break
    
    
        
        




if __name__ == '__main__':
    inicio()