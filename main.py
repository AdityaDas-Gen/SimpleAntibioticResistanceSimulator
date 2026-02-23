import numpy as np
import matplotlib.pyplot as plt
import math as m


#parameters

n0 = 1000.0
k = 1e10
i = 0.25

resistant = [0.0]
susceptible = [n0 -0.0]
antibiotic = 0.1
mutation_rate = 1/1e10
generation = 200




for one in range(generation):
    s = susceptible[-1]
    r = resistant[-1]

    killed_p = antibiotic * s
    mutated_p = mutation_rate * s

    s -= (mutated_p + killed_p)
    r += mutated_p

    K = k - (s + r)

    s_growth = (K / (1 + ((K - s) / s) * np.exp(-i )))
    r_growth = (K/ (1 + ((K - r) / r) * np.exp(-i )))

    susceptible.append(s_growth)
    resistant.append(r_growth)

plt.grid()


plt.scatter(range(generation + 1),resistant, label= "resistant")
plt.scatter(range(generation + 1),susceptible, label= "susceptible")
plt.legend()
plt.show()



