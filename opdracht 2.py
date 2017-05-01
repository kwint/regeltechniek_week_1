import numpy as np
import control
import matplotlib.pylab as plt


def step_info(t, yout):
    print("OS: %f%s" % ((yout.max() / yout[-1] - 1) * 100, '%'))
    print("Tr: %fs" % (t[next(i for i in range(0, len(yout) - 1) if yout[i] > yout[-1] * .90)] - t[0]))
    print(
        "Ts: %fs" % (t[next(len(yout) - i for i in range(2, len(yout) - 1) if abs(yout[-i] / yout[-1]) > 1.02)] - t[0]))


teller = np.array([1.0])
noemer = np.array([1.0, 1.2, 36])
H = control.tf(teller, noemer)
print(H)

Hss = control.tf2ss(H)
print(Hss)

y, t = control.step(H)
step_info(t, y)
plt.plot(t, y)

plt.ylabel("Stap responsie")
plt.xlabel("Tijd [s]")
plt.legend()
plt.show()
