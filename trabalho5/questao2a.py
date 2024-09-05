
from decimal import *
from math import exp

def v2met_euler( f, t0, tf, x0, np ):
    
    # listas para armazenar  a discretização do intervalo 
    # e as aproximações da solução
    t = [t0]
    x = [x0]
    tn = t0
    xn = x0
    
    # tamanho do passo no tempo
    dt = float(tf-t0)/np

    # laço para o avanço no tempo
    for n in range(np):
        # calculo da solução aproximada
        xn = xn + dt*f(tn,xn)
        # atualização do valor do tempo
        tn = t0 + (n+1)*dt
        
        # anexando os valores calculados nas listas
        x.append(xn)
        t.append(tn)
   
    return [t, x]

def v2met_heun( f, t0, tf, x0, np ):
    

    
    t = [t0]
    x = [x0]
    tn = t0
    x1n = x0
    
    dt = float(tf-t0)/np

    for n in range(np):
        xe = x1n + dt*f(tn, x1n)
        x1n = x1n + dt/2*(f(tn, x1n)+f(tn+dt, xe))
        tn = t0 + (n+1)*dt
        
        x.append(x1n)
        t.append(tn)
   
    return [t, x]

def v2runge_kutta4( f, t0, tf, x0, np ):
    
    t = [t0]
    x = [x0]
    tn = t0
    x1n = x0
    
    dt = float(tf-t0)/np

    for n in range(np):
        k1 = dt * f(tn, x1n)
        k2 = dt * f(tn + (1/2) * dt, x1n + (1/2) * k1)
        k3 = dt * f(tn + (1/2) * dt, x1n + (1/2) * k2)
        k4 = dt * f(tn + dt, x1n + k3)

        x1n = x1n + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        tn = t0 + (n+1)*dt
    
        x.append(x1n)
        t.append(tn)
   
    return [t, x]

g = 9.8
m = 75
c = 12.5

def velocidade(x):
  return (g*(m)/(c)) * (1-exp((-c/m)*x))

def func(t, x):
  return g-(c/m)*x

def repetiçoes():
  qtd_euler, qtd_heun, qtd_runge = 1, 1, 1
  velocidade_exata = velocidade(25)
  euler = v2met_euler(func, 0, 25, 0, 1)[-1][-1]
  heun = v2met_heun(func, 0, 25, 0, 1)[-1][-1]
  runge = v2runge_kutta4(func, 0, 25, 0, 1)[-1][-1]

  while abs(velocidade_exata - euler) > 10**-2:
       qtd_euler += 2
       euler = v2met_euler(func, 0, 25, 0, qtd_euler)[-1][-1]
  while abs(velocidade_exata - heun) > 10**-2:
       qtd_heun += 1
       heun = v2met_heun(func, 0, 25, 0, qtd_heun)[-1][-1]
  while abs(velocidade_exata - runge) > 10**-2:
       qtd_runge += 1
       runge = v2runge_kutta4(func, 0, 25, 0, qtd_runge)[-1][-1]
  return qtd_euler, qtd_heun, qtd_runge

rep_euler, rep_heun, rep_runge = repetiçoes()

print(f"A velocidade exata vale {velocidade(25)}")
print(f"A velocidade usando euler vale {v2met_euler(func, 0, 25, 0, rep_euler)[-1][-1]}")
print(f"A velocidade usando heun vale {v2met_heun(func, 0, 25, 0, rep_heun)[-1][-1]}")
print(f"A velocidade usando runge kutta vale {v2runge_kutta4(func, 0, 25, 0, rep_runge)[-1][-1]}")
print(f"O numero de iterações necessarias em euler, heun e runge foram respectivamente: {rep_euler}, {rep_heun}, {rep_runge}")
