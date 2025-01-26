from random import randint, seed
from time import time

import idea1
import idea2
import idea3
import idea4
import idea5

import matplotlib.pyplot as plt


idea_to_module = {
    1: idea1, 
    2: idea2, 
    3: idea3,
    4: idea4,
    5: idea5
}


def generate_input(k):
    seed(9001)
    piles = [randint(1, 10**9) for _ in range(k)]
    h = randint(1, k)
    return (piles, h)


def get_time(n, inp):
    start = time()
    idea_to_module[n].min_eating_speed(*inp)
    return time() - start


def plot_graph(idea, inputs, color):
    n = len(inputs)
    x = [input[0] for input in inputs]
    y = [get_time(idea, inputs[i][1]) for i in range(n)]
    plt.plot(x, y, color=color, label="idea" + str(idea))
    plt.legend(loc='best')


n = 100_000
inputs = [(i, generate_input(i)) for i in range(2, n+1, n//100)]
colors = "cyan green red blue purple".split()
for i in [1, 2, 3, 4, 5]:
    plot_graph(i, inputs, colors[i-1])
plt.show()