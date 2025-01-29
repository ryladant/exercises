import math
import numpy as np

v = [5,-3]
o = 2.667
u = 0

def calculo_angulo_entre_vetores(v,o):
    array_v = np.array([[v[0]],
                        [v[1]]])    

    array_rot = np.array([[np.cos(o), -np.sin(o)],
                          [np.sin(o), np.cos(o)]])

    u = np.dot(array_rot, array_v)

    print(f"O vetor {v} rotacionado em {o} radianos é: ({u[0],u[1]})")

calculo_angulo_entre_vetores(v, o)
