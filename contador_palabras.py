# Dado un texto contar cuantas veces se repite una palabra
# Ejemplo: 
# "A veces las personas de las que nadie espera hace cosas que nadie imagina"
# nadie -> 2 veces 
# que -> 2 veces

def run ():
    
    def transformar_minusculas(t):
        texto = t.lower()
        return (texto) 
    
    def array (t):
        texto = t.split(' ')
        
        return (texto)
    
    def contador(t):
        dictionary = {}

        for word in t:
            if word in dictionary:
                dictionary[word] +=1
            else:
                dictionary[word] = 1    
        
        for i in dictionary:
            print(f'La palabra {i} aparece {dictionary[i]}.')    
        
    
    text = 'A veces las personas de las que nadie espera hace cosas que nadie imagina' 
    texto = transformar_minusculas(text)
    texto_array = array(texto)
    contador(texto_array)



if __name__ == '__main__':
    run()