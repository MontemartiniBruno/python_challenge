from calendar import c


def juego(l):
    c =len(l)
    total = l[0]
    puntaje = 0
    print('Comienza el juego')
    for i in range (0,c-1) :
        aux = i+1
        resultado = int(input(f'Ingrese la suma de {total} + {l[aux]}: '))
        total = total + l[aux]
        if total == resultado:
            puntaje += 1
        else:
            print(f'Perdiste, tu puntaje fue {puntaje}')
            break
    
    if total == resultado:
        print(f'Ganaste! Sumaste {c} numeros sin equivocarte!')


if __name__ == '__main__':
    juego([12,45,87,5,64,3])

