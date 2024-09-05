u = 1.8 * (10**-5)
dict = {
    0: 0, 
    0.002: 0.287, 
    0.006: 0.899, 
    0.012: 1.915, 
    0.018: 3.048, 
    0.024: 4.299
}
def primeiraOrdemAvancada( x, delta):
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

def tensao(y, delta):
  derivada_avancada = primeiraOrdemAvancada(y, delta) 
  tensao = u * derivada_avancada
  return tensao 

resultado = tensao(0, 0.012)

print(f'A tensão de cisalhamento para y valendo 0: {resultado}')



