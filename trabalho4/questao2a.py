from math import sin, pi

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

def f(x):
  #Integral de sin(x) é -cos(x)
  #No intervalo de 0 a pi (180°), encontra-se o valor 2.
  return sin(x)

lista_valores = [10, 50, 100, 200]
lista_func = []
b, a = pi, 0

print("Regra do trapézio e de simpson COM listas\n\n")

for i in lista_valores:
  h = (b - a)/i
  for j in range(i + 1):
    lista_func.append(f(a + j * h))

  print(f"Trapezio para n = {i} é {trapezioA(h, lista_func)}\n")
  print(f"Erro absoluto {abs((2) - trapezioA(h, lista_func))}\n\n")

  print(f"Simpson para n = {i} é {simpsonA(h, lista_func)}\n")
  print(f"Erro absoluto {abs((2) - simpsonA(h, lista_func))}\n\n")


print("\n\nRegra do trapézio e de simpson SEM listas\n\n")
for i in lista_valores:
    
    print(f"Trapezio para n = {i} é {trapezioB(f, a, b, i)}\n")
    print(f"Erro absoluto {abs((2) - trapezioB(f, a, b, i))}\n\n")

    print(f"Simpson para n = {i} é {simpsonB(f, a, b, i)}\n")
    print(f"Erro absoluto {abs((2) - simpsonB(f, a, b, i))}\n\n")