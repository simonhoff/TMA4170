import matplotlib.pyplot as plt
import numpy as np
import math
x_vals = np.linspace(-np.pi,np.pi,100)

order_list = [1,2,5,7]
y = np.zeros([len(order_list),len(x_vals)])

fun = [np.power(x,2) for x in x_vals]

for i in range(len(order_list)):
    for j in range(len(x_vals)):
        y[i][j] = np.power(np.pi,2)/3
        for n in range(1,order_list[i]+1):
            y[i][j] += 4*(np.power(-1,n)/np.power(n,2))*np.cos(n*x_vals[j])

plt.plot(x_vals,fun)
for arr in y:
    plt.plot(x_vals,arr)

plt.show()
