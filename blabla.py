import numpy as np
from tabulate import tabulate
z = lambda t : t**3
zd = lambda t : 3*t**2



kk = list(range (21))
print(kk)


# De lijst hh , gemaakt met behulp van een for - loop .
hh = []; # Lege lijst maken
for k in kk :
    h = 10**( - k )
    hh = hh + [ h ]
 
print(hh)

D = []
dmin = []
for h in hh:
    a = ((z(3 + h) - z(3))/h)
    D += [a]
    dmin += [abs(a - zd(3))]
print(D)
print(dmin)

table = [kk, hh, D, dmin]

print(tabulate(np.transpose(table)))