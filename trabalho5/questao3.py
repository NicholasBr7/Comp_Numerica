import numpy as np

tempo_inicial = 0
tempo_final = 21
pop_suscetivel = 10000
pop_infectada = 1
beta = 0.0003
gamma = 0.15

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


def func(t, x):
  y = [-beta * x[0] * x[1] + gamma * x[1], beta * x[0] * x[1] - gamma * x[1]]
  return np.array([y[0], y[1]])

x0 = [pop_suscetivel, pop_infectada]

t1, valor_x = v2runge_kutta4(func, tempo_inicial, tempo_final, x0, 50)

def valor_erro():
    # O t_anterior e o t_proximo são inúteis. Só servem para armazenar informações

    n = 16
    t_anterior, anterior = v2runge_kutta4(func, tempo_inicial, tempo_final, x0, 15)
    t_proximo, proximo = v2runge_kutta4(func, tempo_inicial, tempo_final, x0, 16)
    
    erro_sus = abs(proximo[-1][0] - anterior[-1][0])
    erro_inf = abs(proximo[-1][1] - anterior[-1][1])

    while erro_sus > 0.05 and erro_inf > 0.05:
        t_anterior, anterior = v2runge_kutta4(func, tempo_inicial, tempo_final, x0, n)
        t_proximo, proximo = v2runge_kutta4(func, tempo_inicial, tempo_final, x0, n+1)
    
        erro_sus = abs(proximo[-1][0] - anterior[-1][0])
        erro_inf = abs(proximo[-1][1] - anterior[-1][1])
        n += 1
    return n

print(f"Dado um tempo de {t1[-1]} dias temos um total de {round(valor_x[-1][0], 3)} suscetíveis e {round(valor_x[-1][1], 3)} infectados para 50 iterações")
print(f"Um erro menor que 0.05 precisa de {valor_erro()} iterações")


