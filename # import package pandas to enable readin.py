# import package pandas to enable reading data
import pandas as pd
import matplotlib.pyplot as plt
T1 = pd.read_csv('humerus-177-outer.csv', skiprows=6).to_numpy()
T2 = pd.read_csv('humerus-177-inner.csv', skiprows=6).to_numpy()

plt.plot(T1[:,0],T1[:,1])
plt.plot(T2[:,0],T2[:,1])

plt.xlim([-10, 13])
plt.ylim([-10, 12])
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.show()