import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,50)

y = x*x*x + 7

plt.plot(x,y,label="oi",color="red", linestyle="-")

plt.show()
