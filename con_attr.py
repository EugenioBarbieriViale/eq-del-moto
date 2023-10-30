# Oscillatore armonico smorzato


import matplotlib.pyplot as plt
import numpy as np
import pandas


N = 1000

# Costants
m = 0.5 # kg
Dt = 0.01 # s
g = 9.81 # m/s2
k = 10 # N/m
c = pow(7.20,-6) # kg/s
A = 10 # m
vi = 0 # m/s

# Arrays
n = range(0,N)
axis = range(0,N+1)

t = [x * Dt for x in axis]
x_in = [A]
v_in = [vi]
F = [-k*A - c*vi]
a = [F[0]/m]
x_fin = []
v_fin = []

# Variables
T = round(2 * np.pi * np.sqrt(m/k),4)
v_ang = np.sqrt(k/m)


for i in n:
    x_fin.append(x_in[i] + v_in[i] * Dt + 0.5 * a[i] * Dt*Dt)
    v_fin.append(v_in[i] + a[i] * Dt)

    F.append(-k * x_in[i] - c * v_in[i])
    a.append(F[i]/m)

    x_in.append(x_fin[i])
    v_in.append(v_fin[i])


# Graph 1
plt.figure()
plt.plot(axis,x_in, label="x_in")
plt.hlines(0,0,N,colors="black")

plt.title("Posizione (Periodo: {}s)".format(str(T)))
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.grid(visible=True)
plt.legend()

# Graph 2
plt.figure()

plt.plot(axis,v_in, label="v_in", color="red")
plt.hlines(0,0,N,colors="black")

plt.title("Velocità (Periodo: {}s)".format(str(T)))
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.grid(visible=True)
plt.legend()

plt.show()
