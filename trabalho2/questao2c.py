import math

lista_delta = [0.1, 0.01, 0.001, 0.0001]

valor_x = 0.4

def f(x):
    equacao = math.sin(math.sqrt(x))/math.sqrt(x)
    return equacao

def f2(x):
    equacao_derivada = (math.cos(math.sqrt(x))/2*x) - (math.sin(math.sqrt)/2*(x**3/2))
    return equacao_derivada

def f3(x):
    equacao_segunda_derivada = -(math.sin(math.sqrt(x))/4*(x**3/2)) - (3*math.cos(math.sqrt)/4*(x**2)) + (3*math.sin(math.sqrt(x))/4*(x**5/2))
    return equacao_segunda_derivada


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



def primeiraOrdemAvancadaLista(f: list, delta):
    '''
    Calcula a derivada de primeira ordem avançada da parte 1 do item i
    '''
    resultado = -f[4] + 4 * f[3] - 3 * f[2]
    resultado /= 2 * delta
    return resultado

def primeiraOrdemCentralLista(f: list, delta):
    ''''
    Calcula a derivada de primeira ordem central da parte 2 do item i
    '''
    resultado = f[3] - f[1]
    resultado /= 2 * delta
    return resultado 

def segundaOrdemAvancadaLista(f:list, delta):
    '''
    Calcula a derivada de segunda ordem avancada da parte 1 do item ii
    '''
    resultado = (-1) * f[5] + 4 * f[4] - 5 * f[3] + 2 * f[2]
    resultado /= (delta ** 2)
    return resultado

def segundaOrdemCentralLista(f: list, delta):
    '''
    Calcula a derivada de segunda ordem central da parte 2 do item ii
    '''
    resultado = f[3] - 2 * f[2] + f[1]
    resultado /= (delta ** 2)
    return resultado

def terceiraOrdemAvancadaLista(f: list, delta):
    '''
    Calcula a derivada de terceira ordem avancada da parte 1 do item iii
    '''
    resultado = (-3) * f[6] + 14 * f[5] - 24 * f[4] + 18 * f[3] - 5 * f[2]
    resultado /= 2*(delta ** 3) 
    return resultado 

def terceiraOrdemCentralLista(f: list, delta):
    '''
    Calcula a derivada de terceira ordem central da parte 2 do item iii
    '''
    resultado = f[4] - 2 * f[3] + 2 * f[1] - f[0]
    resultado /= 2 * (delta ** 3)
    return resultado


def criar_lista(x, delta):
    l = [f(x - 2*delta), f(x - delta), f(x), f(x + delta),
         f(x + 2*delta), f(x + 3*delta), f(x + 4*delta)]
    return l


def primeira_derivada(valor_x, lista_delta):

    resposta_primeira_derivada = f(valor_x)
    print(f"Resposta primeira derivada: {resposta_primeira_derivada}\n")

    for valor in lista_delta:

        #sem lista
        primeira_ordem_avancada = primeiraOrdemAvancada(f, valor_x, valor)
        primeira_ordem_central = primeiraOrdemCentral(f, valor_x, valor)

        #com lista
        lista_x = criar_lista(valor_x, valor)
        primeira_ordem_avancada_lista = primeiraOrdemAvancadaLista(lista_x, valor)
        primeira_ordem_central_lista = primeiraOrdemCentralLista(lista_x, valor)


        #Erro absoluto sem lista
        print(f"O erro absoluto para delta {valor} sem lista avançada foi: {resposta_primeira_derivada - primeira_ordem_avancada}")
        print(f"O erro absoluto para delta {valor} sem lista central foi: {resposta_primeira_derivada - primeira_ordem_central}\n")

        #Erro absoluto com lista
        print(f"O erro absoluto para delta {valor} com lista avançada foi: {resposta_primeira_derivada - primeira_ordem_avancada_lista}")
        print(f"O erro absoluto para delta {valor} com lista avançada foi: {resposta_primeira_derivada - primeira_ordem_central_lista}\n")

primeira_derivada(valor_x=valor_x, lista_delta=lista_delta)