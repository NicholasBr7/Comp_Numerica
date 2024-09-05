def met_euler(f, t0, tf, x0, n):
    np = float(tf - t0)/n
    yn = x0

    for i in range(1, n):
        yn = yn + np * f(yn)
    return yn


#Usando o metodo de euler fornecido pelo professor
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