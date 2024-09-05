from math import sin, sqrt


def f(x):
    equacao = sin(sqrt(x))/sqrt(x)
    return equacao

def primeiraOrdemAvancada(f: list, delta):
    '''
    Calcula a derivada de primeira ordem avançada da parte 1 do item i
    '''
    resultado = -f[4] + 4 * f[3] - 3 * f[2]
    resultado /= 2 * delta
    return resultado

def primeiraOrdemCentral(f: list, delta):
    ''''
    Calcula a derivada de primeira ordem central da parte 2 do item i
    '''
    resultado = f[3] - f[1]
    resultado /= 2 * delta
    return resultado 

def segundaOrdemAvancada(f:list, delta):
    '''
    Calcula a derivada de segunda ordem avancada da parte 1 do item ii
    '''
    resultado = (-1) * f[5] + 4 * f[4] - 5 * f[3] + 2 * f[2]
    resultado /= (delta ** 2)
    return resultado

def segundaOrdemCentral(f: list, delta):
    '''
    Calcula a derivada de segunda ordem central da parte 2 do item ii
    '''
    resultado = f[3] - 2 * f[2] + f[1]
    resultado /= (delta ** 2)
    return resultado

def terceiraOrdemAvancada(f: list, delta):
    '''
    Calcula a derivada de terceira ordem avancada da parte 1 do item iii
    '''
    resultado = (-3) * f[6] + 14 * f[5] - 24 * f[4] + 18 * f[3] - 5 * f[2]
    resultado /= 2*(delta ** 3) 
    return resultado 

def terceiraOrdemCentral(f: list, delta):
    '''
    Calcula a derivada de terceira ordem central da parte 2 do item iii
    '''
    resultado = f[4] - 2 * f[3] + 2 * f[1] - f[0]
    resultado /= 2 * (delta ** 3)
    return resultado


def lista(x, delta):
    lista = [f(x - (2 * delta)), f(x - delta), f(x), f(x + delta),
         f(x + (2 * delta)), f(x + (3 * delta)), f(x + (4 * delta))]
    return lista