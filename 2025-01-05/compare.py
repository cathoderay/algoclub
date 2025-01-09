from random import randint
from time import time

import idea1

import matplotlib.pyplot as plt


idea_to_module = { 
    1: idea1
}


def generate_input(n):
    return [randint(0, n) for _ in range(n)]


def get_time(n, inp):
    start = time()
    idea_to_module[n].sort(inp)
    return time() - start


def plot_graph(idea, inputs, color):
    n = len(inputs)
    x = list(range(1, n))
    y = [get_time(idea, inputs[i]) for i in range(1, n)]
    plt.plot(x, y, color=color, label="buble sort")
    plt.legend(loc='best')


n = 1_000
inputs = [generate_input(i) for i in range(n)]
colors = "blue green yellow black cyan brown red purple".split()
for i in range(1, 2):
    plot_graph(i, inputs, colors[i-1])
plt.show()