from random import randint
from time import time

import idea1
import idea2
import idea3
import idea4

import matplotlib.pyplot as plt


idea_to_module = {
    1: idea1, 2: idea2, 3: idea3, 4: idea4,
}


def generate_input(k):
    m = randint(0, k)
    n = k - m
    nums1 = [randint(0, k) for _ in range(m)]
    nums2 = [randint(0, k) for _ in range(n)]
    nums1.sort()
    nums2.sort()
    nums1 = nums1 + [0]*n
    return (nums1, m, nums2, n)


def get_time(n, inp):
    start = time()
    idea_to_module[n].merge(*inp)
    return time() - start


def plot_graph(idea, inputs, color):
    n = len(inputs)
    x = [input[0] for input in inputs]
    y = [get_time(idea, inputs[i][1]) for i in range(n)]
    plt.plot(x, y, color=color, label="idea" + str(idea))
    plt.legend(loc='best')


n = 1_000_000
inputs = [(i, generate_input(i)) for i in range(0, n+1)]
colors = "cyan green red blue purple".split()
for i in [3, 2, 1]:
    plot_graph(i, inputs, colors[i-1])
plt.show()