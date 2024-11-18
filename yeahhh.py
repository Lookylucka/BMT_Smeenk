import numpy as np ;

list = []
for k in range (51):
    list.append(k**2)

print(list)


som = np.sqrt(8) + np.sqrt(18)
for n in range (4,50):
    if som < 1000:
        oordeel = 'valt binnen de 1000'
        print(n)
        print(oordeel)
        som += np.sqrt(n**3)
        
    elif som >= 1000:
        print('Vanaf hier niet meer haha')
        print(n)
        break

n = n - 1
print(n)
print("is het hoogste getal dat zorgt voor een totale som binnen de 1000")
