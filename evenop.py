# import packages
import numpy as np
import matplotlib.pyplot as plt
# Define angle theta and next r as a fucntion of theta.
import pandas as pd
T1 = pd.read_csv('humerus-177-outer.csv', skiprows=6).to_numpy()
T2 = pd.read_csv('humerus-177-inner.csv', skiprows=6).to_numpy()
plt.plot(T1[:,0],T1[:,1])
plt.plot(T2[:,0],T2[:,1])

theta = np.arange(0, 2*np.pi, 0.05)
a = 0.125
R = 8.6
gamma = 3.7


r0 = R * (1 + a*np.cos(3 * (theta - gamma)))
r1 = (r0 * np.cos(theta))
r2 = (r0 * np.sin(theta))
u = np.sqrt(r1 + r2)
#Create the plot
plt.plot(r1, r2)

plt.xlim([-10, 13])
plt.ylim([-10, 12])
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.show()