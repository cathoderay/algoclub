from random import randint
from time import time

import idea1
import idea2

import matplotlib.pyplot as plt


def generate_input(n):
    return [randint(0, 10000) for _ in range(n)]


def get_time(n, inp):
    idea_to_module = {1: idea1, 2: idea2}
    start = time()
    idea_to_module[n].solve(inp)
    return time() - start


def plot_graph(idea, n, color):
    x = list(range(1, n))
    y = [
        get_time(idea, generate_input(i))
        for i in range(1, n)
    ]
    plt.plot(x, y, color=color)


plot_graph(1, 100, "red")
plot_graph(2, 100, "green")
plt.show()