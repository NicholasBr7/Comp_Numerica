# Computação Numérica
# questão 3 - b

# def primeiraDerivadaCentralPonto(function, y, delta):
#     resultado = function(y + delta) - function(y - delta) 
#     resultado /= (2 * delta)
#     return resultado

# def segundaDerivadaCentralPonto(function, y, delta):
#     resultado = function(y + delta) - 2 * function(y) + function(y - delta)
#     resultado /= (delta ** 2)
#     return resultado

# values = {
#     0: 0,
#     2: 0.7,
#     4: 1.8,
#     6: 3.4, 
#     8: 5.1,
#     10: 6.3,
#     12: 7.3,
#     14: 8,
#     16: 8.4,
# }

# def valores(y, values, delta):
#     derivada_velocidade = primeiraDerivadaCentralPonto(values, y, delta)
#     derivada_aceleração = segundaDerivadaCentralPonto(values, y, delta)
#     print(f"velocidade em t = 10 vale {derivada_velocidade}\n")
#     print(f"a aceleração em t = 10 vale {derivada_aceleração}")

# for delta_x in [2, 4, 6]:
#     valores(10, values, delta_x)


dict = {
    0: 0,
    2: 0.7,
    4: 1.8,
    6: 3.4, 
    8: 5.1,
    10: 6.3,
    12: 7.3,
    14: 8,
    16: 8.4,
}
def primeiraOrdemAvancada(x, delta):
    '''
    Calcula a derivada de primeira ordem avançada da parte 1 do item i
    '''
    resultado1 = x + (2 * delta)
    y1 = dict.get(resultado1)
    resultado2 = x + delta
    y2 = dict.get(resultado2)
    resultado3 = x
    y3 = dict.get(resultado3)

    resultado = - y1 + 4 * y2 - 3 * y3
    resultado /= 2 * delta
    return resultado

def segundaOrdemAvancada(x, delta):
    resultado1 = x + (3 * delta)
    y1 = dict.get(resultado1)
    resultado2 = x + (2 * delta)
    y2 = dict.get(resultado2)
    resultado3 = x + delta
    y3 = dict.get(resultado3)
    resultado4 = x
    y4 = dict.get(resultado4)

    resultado = - y1 + 4 * y2 - 5 * y3 + 2 * y4
    resultado /= (delta ** 2)
    return resultado

def calculo(y, delta):
  derivada_primeira_avancada = primeiraOrdemAvancada(y, delta) 
  derivada_segunda_avancada = segundaOrdemAvancada(y, delta)
  return derivada_primeira_avancada, derivada_segunda_avancada

velocidade, aceleracao = calculo(10, 2)

print(f'A velocidade encontrada foi: {velocidade}. A aceleração foi: {aceleracao}')