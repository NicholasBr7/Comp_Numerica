#Questão 1 - a

listaX = [0.5, 1, 2, 3]
listaY = [1, 2, -1, 4]

def lagrange(lx, ly, x): 
  p = 0
  n = len(lx)
  for i in range(n):  #somatorio
    produto = 0

    for j in range(n): #produtorio
      if(i != j):
        if(produto == 0):
          produto = (x - lx[j]) / (lx[i] - lx[j])
          continue
    
        produto *= (x - lx[j])/(lx[i] - lx[j])

    p += ly[i]*produto
  
  return p

def testa(lx, ly, x):
  print(f"Resultado 'nicholas' de lagrange é: {lagrange(lx, ly, x)}")

testa(listaX, listaY, 0.5)
testa(listaX, listaY, 1)
testa(listaX, listaY, 3)

