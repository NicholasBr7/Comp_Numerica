from math import sin, sqrt

def f(x):
    equacao = sin(sqrt(x))/sqrt(x)
    return equacao

def primeiraOrdemAvancada(f, x, delta):
    '''
    Calcula a derivada de primeira ordem avançada da parte 1 do item i
    '''
    resultado = -f(x + (2 * delta)) + 4 * f(x + delta) - 3 * f(x)
    resultado /= 2 * delta
    return resultado

def primeiraOrdemCentral(f, x, delta):
    ''''
    Calcula a derivada de primeira ordem central da parte 2 do item i
    '''
    resultado = f(x + delta) - f(x - delta)
    resultado /= 2 * delta
    return resultado 

def segundaOrdemAvancada(f, x, delta):
    '''
    Calcula a derivada de segunda ordem avancada da parte 1 do item ii
    '''
    resultado = -f(x + (3 * delta)) + 4 * f(x + (2 * delta)) - 5 * f(x + delta) + 2 * f(x)
    resultado /= (delta ** 2)
    return resultado

def segundaOrdemCentral(f, x, delta):
    '''
    Calcula a derivada de segunda ordem central da parte 2 do item ii
    '''
    resultado = f(x + delta) - 2 * f(x) + f(x - delta)
    resultado /= (delta ** 2)
    return resultado


def terceiraOrdemAvancada(f, x, delta):
    '''
    Calcula a derivada de terceira ordem avancada da parte 1 do item iii
    '''
    resultado = -3 * f(x + (4 * delta)) + 14 * f(x + (3 * delta)) - 24 * f(x + (2 * delta)) + 18 * f(x + delta) -5 * f(x)
    resultado /= 2*(delta ** 3) 
    return resultado 

def terceiraOrdemCentral(f, x, delta):
    '''
    Calcula a derivada de terceira ordem central da parte 2 do item iii
    '''
    resultado = f(x + (2 ** delta)) - 2 * f(x + delta) + 2 * f(x - delta) - f(x - (2 * delta))
    resultado /= 2 * (delta ** 3)
    return resultado

