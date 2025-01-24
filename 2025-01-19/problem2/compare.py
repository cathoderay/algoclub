from random import randint
from time import time

import idea1
import idea2


import matplotlib.pyplot as plt


idea_to_module = {
    1: idea1, 2: idea2
}


def generate_input(k):
    m = randint(1, k-1)
    n = k - m
    nums1 = [randint(1, k) for _ in range(m)]
    nums2 = [randint(1, k) for _ in range(n)]
    return (nums1, nums2)


def get_time(n, inp):
    start = time()
    idea_to_module[n].xor_all_nums(*inp)
    return time() - start


def plot_graph(idea, inputs, color):
    n = len(inputs)
    x = [input[0] for input in inputs]
    y = [get_time(idea, inputs[i][1]) for i in range(n)]
    plt.plot(x, y, color=color, label="idea" + str(idea))
    plt.legend(loc='best')


n = 10_000
inputs = [(i, generate_input(i)) for i in range(3, n+1)]
colors = "green blue".split()
for i in [1, 2]:
    plot_graph(i, inputs, colors[i-1])
plt.show()