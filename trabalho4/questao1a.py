#Item a - Abordagem com lista

def trapezioA(h, lista):
    tamanho = len(lista)
    soma = 0

    for i in range(1, tamanho - 1):
        soma += 2 * lista[i]
    resultado = (h/2) * (lista[0] + lista[tamanho - 1] + soma)
    return resultado

def simpsonA(h, lista):
    tamanho = len(lista)
    soma = 0

    for i in range(1, tamanho - 1):
        if i % 2 == 0:
            soma += 2 * lista[i]
        else:
            soma += 4 * lista[i]
    resultado = (h/3) * (lista[0] + lista[tamanho - 1] + soma)
    return resultado


#Item b - Abordagem sem lista


def trapezioB(f, a, b, n):
    h = (b - a)/n
    soma = 0

    for i in range(1,n):
        k = a + i * h
        soma += 2*f(k)

    resultado = (h/2) * (f(a) + f(b) + soma)
    return resultado

def simpsonB(f, a, b, n):
    h = (b - a)/n
    soma = 0
    
    for i in range(1,n):
        k = a + i * h
        if i % 2 == 0:
            soma += 2 * f(k)
        else:
            soma += 4 * f(k)

    resultado = (h/3) * (f(a) + f(b) + soma)
    return resultado