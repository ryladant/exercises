import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 100)

y = x*x + 3

plt.plot(x, y, label="y=x²+3", color="red", linestyle="-")

plt.legend()
plt.show()
