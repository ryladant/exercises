import math
import numpy as np

def main():
    pegar_inputs_usuario()

def transformar_angulo_graus_rad(o):
    return math.radians(o) 

def pegar_inputs_usuario():
    x, y = map(float, input("Digite o vetor 2D (x y): ").split())
    o = float(input("Digite o angulo de rotacao (em graus): "))
    calculo_angulo_entre_vetores(np.array([x, y]), o)

def calculo_angulo_entre_vetores(v,o):
    o = transformar_angulo_graus_rad(o)
    array_v = np.array(v)    
    array_rot = np.array([[np.cos(o), -np.sin(o)],
                          [np.sin(o), np.cos(o)]])

    u = np.round(np.dot(array_rot, array_v), decimals=3)

    print(f"O vetor [{v[0]:.3f}, {v[1]:.3f}] rotacionado em {o:0.5f} radianos é:[{u[0]:.3f}, {u[1]:.3f}]")

main()
