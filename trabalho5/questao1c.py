def runge_kutta4(f, t0, tf, x0, n):
    np = float(tf - t0)/n
    yn = x0

    for i in range(1, n):
        k1 = np * f(yn)
        k2 = np * f(yn + (k1 * (1/2)))
        k3 = np * f(yn + (k2 * (1/2)))
        k4 = np * f(yn + k3)
        yn = yn + (1/6) * (k1 + 2*k2 + 2*k3 + k4) 
    return yn

#Usando o metodo de euler fornecido pelo professor

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