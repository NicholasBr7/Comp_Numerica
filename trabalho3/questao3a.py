#Questão 3 - a
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

def testa_lagrange(lx, ly, x):
  print(f"Resultado de lagrange é: {lagrange(lx, ly, x)}")

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

def testa_newton(lx, ly, x):
	print(f"Resultado de newton é: {polinomio_newton(lx, ly, x)}")

x = 4
y = 3.2

dicionario = {
    "x0": [100, 85, 70, 55, 40],
    "x2": [90, 64.49, 48.9, 38.78, 35],
    "x4": [80, 53.5, 38.43, 30.39, 30],
    "x6": [70, 48.15, 35.03, 27.07, 25.00],
    "x8": [60, 50, 40, 30, 20]
}

ly_linear = [2, 4]
lz_linear = [53.50, 38.43]

print("Linear ")
testa_lagrange(ly_linear, lz_linear, y)
testa_newton(ly_linear, lz_linear, y)

ly_quadratico = [2, 4, 6]
lz_quadratico = [53.50, 38.43, 30.39]

print("Quadratica ")
testa_lagrange(ly_quadratico, lz_quadratico, y)
testa_newton(ly_quadratico, lz_quadratico, y)

ly_cubico = [0, 2, 4, 6]
lz_cubico = [80, 53.50, 38.43, 30.39]

print("Cúbica ")
testa_lagrange(ly_cubico, lz_cubico, y)
testa_newton(ly_cubico, lz_cubico, y)