import random
import sys


n = 100000
mini = random.randint(0, 1000)
maxi = random.randint(0, 10000)
if mini > maxi: 
    mini, maxi = maxi, mini
sys.stdout.write(' '.join(map (str, list(random.randint(mini, maxi) for i in range(n)))) + "\n")