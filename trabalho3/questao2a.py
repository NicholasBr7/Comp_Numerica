#Questão 2 - a
import numpy as np

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

    erro_Lagrange = erroInterpolacao(ly,poli_Lagrange)
    erro_Newton = erroInterpolacao(ly, poli_Newton)

    print(f"PARA N = {k} \n\nValores de Runge \n\n{ly}\n\nInterpolação de Lagrange \n\n{poli_Lagrange} \n\nCom erro igual a {erro_Lagrange} \n\nInterpolação de Newton \n\n {poli_Newton} \n\nCom erro igual a {erro_Newton}\n\n")



#Usando pontos de controle

def pontosDeControle():
  
  lista = []
  for j in range(101): 
    xj = (-1) + (((2 * j)+1)/100)
    lista.append(xj)
  return lista

x = pontosDeControle()
y = tabelarFx(runge, x)

poli_Lagrange2 = []
poli_Newton2 = []
for i in range(len(x)):
    poli_Lagrange2.append(lagrange(lx, ly, i))
    poli_Newton2.append(polinomio_newton(lx, ly, i))

erro_Lagrange2 = erroInterpolacao(y, poli_Lagrange2)
erro_Newton2 = erroInterpolacao(y, poli_Newton2)

print(f"USANDO OS PONTOS DE CONTROLE \n\nErro para lagrange igual a {erro_Lagrange2} \n\nErro para Newton igual a {erro_Newton2}\n\n")
