from math import cos, pi
from decimal import *

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

def fresnel(x):
    return cos((pi*x**2)/2)

def fresnel_trapezio(x, valor):
    n = 10
    trapezio = 0
    while(abs(trapezio - valor) >= 10**-8):
      n += 200
      trapezio = trapezioB(fresnel, 0, x, n)
    return trapezio, n

def fresnel_simpson(x, valor):
    n = 10
    simpson = 0
    while(abs(simpson - valor) >= 10**-8):
      n += 10
      simpson = simpsonB(fresnel, 0, x, n)
    return simpson, n

x = [-2, 0.5, 1, 5]
y = [-0.48825340607534075450, 0.49234422587144639288, 0.77989340037682282947, 0.56363118870401223110]

for i in range(len(x)):
    fresnel_trap, pontos_trap = fresnel_trapezio(x[i], y[i])
    fresnel_simp, pontos_simp = fresnel_simpson(x[i], y[i])
    erro_trap = Decimal(abs(fresnel_trap - y[i]))
    erro_simp = Decimal(abs(fresnel_simp - y[i]))

    print(f"O valor de fresnel no ponto {x[i]} usando trapézio é {fresnel_trap}")
    print(f"O erro absoluto é {erro_trap}")
    print(f"O numero de pontos usados em trapézio foi {pontos_trap}\n\n")


    print(f"O valor de fresnel no ponto {x[i]} usando simpson é {fresnel_simp}")
    print(f"O erro absoluto é {erro_simp}")
    print(f"O numero de pontos usados em simpson foi {pontos_simp}\n\n")

