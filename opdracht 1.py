import numpy as np
import control
import matplotlib.pylab as plt

teller = np.array([1.0])
noemer = np.array([1.0, -1.0])
H = control.tf(teller, noemer)
print(H)
print(H.pole(), H.zero())

print("Hoi")
Hss = control.tf2ss(H)
print(Hss)
#test1123
K = [0.1, 1, 2, 10]

for i in range(0, len(K)):
    Sys1 = K[i]*H
    Sys2 = 1
    Hclosed = control.feedback(Sys1, Sys2)
    print(i, Hclosed.pole())
    y, t = control.step(Hclosed)
    plt.plot(t, y, label=str(K[i]))
    print(i, y, t)
    print()

plt.ylabel("Stap responsie")
plt.xlabel("Tijd [s]")
plt.yscale("log")
plt.legend()
plt.show()

