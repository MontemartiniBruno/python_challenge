# Escribir los numeros del 1 a un numero específico.
# Para los múltiplos de 3 imprimir buzz, para los de 5 fizz, si es multiplo de ambos buzzfizz

def buzz_feez(n):
    for i in range (1,n+1):
        if i % 3 == 0:
            if i % 5 ==0:
                print('buzzfizz')
            else: 
                print('buzz')
        elif i % 5 == 0:
            print('fizz')
        else:
            print(i)
    
buzz_feez(150)
