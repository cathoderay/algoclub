from random import randint
from time import time

import idea1
import idea2
import idea3
import idea4
import idea5
import idea6

import matplotlib.pyplot as plt


idea_to_module = {
    1: idea1, 2: idea2, 3: idea3,
    4: idea4, 5: idea5, 6: idea6
}


def generate_input(n):
    return randint(-2_147_483_648, 2_147_483_648 - 1)


def get_time(n, inp):
    start = time()
    idea_to_module[n].is_palindrome(inp)
    return time() - start


def plot_graph(idea, inputs, color):
    n = len(inputs)
    x = list(range(1, n))
    y = [get_time(idea, inputs[i]) for i in range(1, n)]
    plt.plot(x, y, color=color, label="idea" + str(idea))
    plt.legend(loc='best')


n = 100
inputs = [generate_input(i) for i in range(n)]
colors = "cyan green yellow black blue brown red purple".split()
for i in range(1, 7):
    plot_graph(i, inputs, colors[i-1])
plt.show()