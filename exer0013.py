# Exemplo simples plotando um vetor

import numpy as np
import matplotlib.pyplot as plt

def main():
    set_vector()

def set_vector():
    print('Digite o x do vetor')
    x = int(input())

    print('Digite o y do vetor')
    y = int(input())

    draw_graph(x, y)

def draw_graph(x, y):
    plt.quiver(0,0,x,y,angles='xy',scale_units='xy',scale=1,color='red')

    plt.ylim(-y-2,y+2)
    plt.xlim(-x-2,x+2)

    plt.legend(loc='lower left', title='Seu vetor')
    plt.grid()
    plt.title(f'Grafico do vetor ({x}, {y})')
    plt.show()

main()
