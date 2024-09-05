import numpy as np

listaX = [0.5, 1, 2]
listaY = [1, 2, -1]

def diferencaDividida(lx, ly):

    #Usei o numpy, pois ele permite trabalhar com operações numéricas de maneira mais simples. 
    #Sem ele, precisaria de variáveis para armazenar o valor do array e de mais loops para trabalhar com elas.
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

def testa(lx, ly, x):
	print(f"Resultado de newton é: {polinomio_newton(lx, ly, x)}")

testa(listaX, listaY, 1)
testa(listaX, listaY, 2)
