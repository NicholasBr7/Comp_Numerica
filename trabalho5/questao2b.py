from questao2a import *

g = 9.8
m = 75
c = 12.5
a = 0.2
b = 1.1
vmax = 46

def C(x):
  return c * ((1 + a*(x/vmax)**b))

def fb(t, x):
  return g-(C(x)/m)*x

rep_euler, rep_heun, rep_runge = repetiçoes()

a2 = v2met_euler(fb, 0, 25, 0, rep_euler)[-1][-1]
b2 = v2met_heun(fb, 0, 25, 0, rep_heun)[-1][-1]
c2 = v2runge_kutta4(fb, 0, 25, 0, rep_runge)[-1][-1]

print(f"O valor encontrado com euler foi de {a2}")
print(f"O valor encontrado com heun foi de {b2}\n")
print(f"O valor encontrado com runge kutta foi de {c2}\n")