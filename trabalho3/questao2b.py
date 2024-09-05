#Questão 2 - b
import numpy as np
from math import cos, pi

def lagrange(lx, ly, x):

    n = len(lx)
    resultado = 0
    for i in range(n):
        anterior = 1
        
        for j in range(n):
            if i != j:
                anterior *= (x - lx[j]) / (lx[i] - lx[j])
        
        resultado += anterior * ly[i]    

    return resultado


def diferencaDividida(lx, ly):

    t = len(lx)
    array_x = np.copy(lx)
    array_y = np.copy(ly)
    for i in range(1, t):
        array_y[i:t] = (array_y[i:t] - array_y[i - 1])/(array_x [i:t] - array_x [i - 1])
    return array_y

def polinomio_newton(lx, ly, x):

    array_y = diferencaDividida(lx, ly)
    n = len(lx) - 1
    resultado = array_y[n]
    for i in range(1, n + 1):
        resultado = array_y[n-i] + (x - lx[n-i]) * resultado
    return resultado


def runge(x):
  
  #Função runge dada no enunciado
  return 1/(1 + 25 *(x ** 2))

def pontos_listaX(n):
  
  #Polinômio interpolador o qual é calculado para cada n pedido
  lista = []
  for i in range(n): 
    x = (-1) + ((2*i)/n)
    lista.append(x)
  return lista

def tabelarFx(funcao, x):
  
  #Aplica o valor da lista obtida pelo polinômio na função runge
  lista = []
  for valor in x:
    lista.append(funcao(valor))
  return lista

def erroInterpolacao(fx, px):
  
  l = []
  for i in range(len(fx)):
    erro = abs(fx[i]-px[i])
    l.append(erro)
  return max(l)

for k in [5, 10, 15, 20]:
  
    lx = pontos_listaX(k)
    ly = tabelarFx(runge, lx)

    poli_Lagrange = []
    poli_Newton = []

    for i in lx:
        poli_Lagrange.append(lagrange(lx, ly, i))
        poli_Newton.append(polinomio_newton(lx, ly, i))


#Usando nós de Chebyshev

def pontosChebyshev(n): 
    
    lista = []
    for i in range(n):
      x = cos((i * pi)/n)
      lista.append(x)
    return lista

for k in [5, 10, 15, 20]:
    
    lx = pontosChebyshev(k)
    ly = tabelarFx(runge, lx)

    poli_Lagrange = []
    poli_Newton = []
  
    for i in lx:
        poli_Lagrange.append(lagrange(lx, ly, i))
        poli_Newton.append(polinomio_newton(lx, ly, i))

    erroLagrange = erroInterpolacao(ly, poli_Lagrange)
    erroNewton = erroInterpolacao(ly, poli_Newton)

    print(f"USANDO CHEBYSHEV = {k} \n\nValores de Runge \n\n{ly}\n\nInterpolação de Lagrange \n\n{poli_Lagrange} \n\nCom erro igual a {erroLagrange} \n\nInterpolação de Newton \n\n {poli_Newton} \n\nCom erro igual a {erroNewton}\n\n")
