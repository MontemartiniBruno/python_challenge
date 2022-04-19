# Haz una funcion multiplicacion sin usar el simbolo multiplicar

def multiplicar_por(n, c):
    # n y c son los dos factores del producto
    result = n
    for i in range(c-1):
        result += n
    print(result)

multiplicar_por(3,100)