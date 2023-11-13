# Oscillatore armonico smorzato


import matplotlib.pyplot as plt
import numpy as np
import pandas


N = 5000

# Costants
m = pow(4,-7) # kg
Dt = 0.01 # s
g = 9.81 # m/s2
c = pow(7.20,-6) # kg/s
vi = 0 # m/s

# Arrays
n = range(0,N)
axis = range(0,N+1)

t = [x * Dt for x in axis]
x_in = [0]
v_in = [vi]
F = [m*g - c*vi]
a = [F[0]/m]
x_fin = []
v_fin = []

ki = [0.5*m*vi**2]
u = [m*g*x_in[0]]
em = [ki[0]+u[0]]

for i in n:
    x_fin.append(x_in[i] + v_in[i] * Dt - 0.5 * a[i] * Dt*Dt)
    v_fin.append(v_in[i] + a[i] * Dt)

    F.append(m * g - c * v_in[i])
    a.append(F[i]/m)

    x_in.append(x_fin[i])
    v_in.append(v_fin[i])

    ki.append(0.5 * m * v_in[i]**2)
    u.append(m * g * x_in[i])
    em.append(ki[i] + u[i])

# Graph 1
plt.figure()
plt.plot(axis,x_in, label="x_in")

plt.title("Posizione")
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid(visible=True)
plt.legend()

# Graph 2
plt.figure()
plt.plot(axis,v_in, label="v_in", color="red")

plt.title("Velocità")
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.grid(visible=True)
plt.legend()

# Mechanical energy
plt.figure()
plt.plot(axis,em, label="em")
plt.hlines(0,0,N,colors="black")

plt.title("Energia meccanica")
plt.xlabel("t(s)")
plt.ylabel("e(J)")
plt.grid(visible=True)
plt.legend()

plt.show()
