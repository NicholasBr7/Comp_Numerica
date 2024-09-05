def met_heun(f, t0, tf, x0, n):
    np = float(tf - t0)/n
    yn = x0

    for i in range(1, n):
        k1 = np * f(yn)
        k2 = np * f(yn + k1)
        yn = yn + (k1 + k2) * 1/2
    return yn

#Usando o metodo de euler fornecido pelo professor
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

